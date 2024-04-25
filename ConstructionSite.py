import unreal

for component in site.get_components_by_class(unreal.ActorComponent):
    print(component)