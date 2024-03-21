from mechanize import Item

# Hack to bypass select form control


def bypass_select(form, select_name, value):
    select_control = form.find_control(name=select_name)

    select_control.items.append(
        Item(select_control, {"name": value, "value": value})
    )
