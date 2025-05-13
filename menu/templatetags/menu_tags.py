from django import template
from django.urls import resolve
from django.utils.safestring import mark_safe
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # ПОЛУЧАЕМ ТЕКУЩИЙ ПУТЬ
    request = context['request']
    current_path = request.path
    try:
        resolved_name = resolve(current_path).url_name
    except:
        resolved_name = None

    # ТЕПЕРЬ ВСЕ ПУНКТЫ МЕНЮ В 1 ЗАПРОС select_related для oto, prefetch_related для otm, order в какой очередности отображаем
    items = MenuItem.objects.filter(menu__name=menu_name)\
        .select_related('parent')\
        .prefetch_related('children')\
        .order_by('order')
    # для каджого пункта добавляем дочерние idшки
    item_map = {item.id: item for item in items}
    children_map = {}
    for item in items:
        children_map.setdefault(item.parent_id, []).append(item)
    root_items = children_map.get(None, [])
    # ищем активный пункт меню если условие выполняется то элемент - active иначе нифига не active
    active_item = None
    for item in items:
        if item.get_url() == current_path or item.named_url == resolved_name:
            active_item = item
            break
    # Смотрим чо нада развернуть
    active_path = []
    if active_item:
        current = active_item
        while current:
            active_path.insert(0, current)
            current = current.parent
    # Отображаем меню 
    active_ids = {item.id for item in active_path}
    show_children_of = {item.id for item in active_path}
    # рендеринг хтмл
    def render(items, parent_id=None):
        html = ''
        for item in items:
            is_active = item.id in active_ids
            classes = []
            if is_active:
                classes.append('active')
            if item.id in show_children_of and children_map.get(item.id):
                classes += ['has-children', 'expanded']
                submenu = render(children_map.get(item.id, []), parent_id=item.id)
            else:
                submenu = ''

            class_attr = f' class="{" ".join(classes)}"' if classes else ''
            html += f'<li{class_attr}><a href="{item.get_url()}">{item.name}</a>'
            if submenu:
                html += f'<ul>{submenu}</ul>'
            html += '</li>'
        return html

    return mark_safe(f'<ul class="menu">{render(root_items)}</ul>')
