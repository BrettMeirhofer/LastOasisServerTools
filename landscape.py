import unreal

all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

landscape_proxies = [actor for actor in all_actors if isinstance(actor, unreal.LandscapeProxy)]


for landscape_proxy in landscape_proxies:
    print(landscape_proxy.get_editor_property("BodyInstance"))
    body = landscape_proxy.get_editor_property("BodyInstance")
    body.set_editor_property("CollisionProfileName", "UI")
    landscape_proxy.set_editor_property("LandscapeHoleMaterial", landscape_proxy.get_editor_property("LandscapeMaterial"))