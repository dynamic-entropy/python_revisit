# from plugins import add, multiply

# addObj = add.Plugin(5, key={20, 20})
# mulObj = multiply.Plugin(10, key={30, 43})

# print(addObj.execute(10, 20))
# print(mulObj.execute(20, 30))
PLUGINS = ["plugins.add", "plugins.multiply"]


try:
    import importlib
    for name in PLUGINS:
        plug_module = importlib.import_module(name)
        plug_obj = plug_module.Plugin(10, key={10, 20, 30})
        plug_obj.execute(10, 20)
except AttributeError:
    pass

try:
    import imp
    for name in PLUGINS:
        name = name.split('.')[1]
        fp, pathname, description = imp.find_module("plugins")
        P = imp.load_module("plugins", fp, pathname, description)

        fp, pathname, description = imp.find_module(
            name, [pathname])
        plug_module = imp.load_module(name, fp, pathname, description)

        plug_obj = plug_module.Plugin(10, key={10, 20, 30})
        plug_obj.execute(10, 20)

except AttributeError:
    pass

print("Done")
