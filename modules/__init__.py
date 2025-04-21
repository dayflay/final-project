# note that this only works since the ./modules directory is known to have no subdirectories
# if a subdirectory is ever added, you will need to account for that package's __all__
# I'm just too lazy to do it

from importlib import import_module
from pkgutil import iter_modules

__all__ = []

for loader, module_name, is_pkg in iter_modules(__path__):
	module = import_module(f"{__name__}.{module_name}")
	globals()[module_name] = module
	public_symbols = [k for k in dir(module) if not k.startswith("_")]

	for symbol in public_symbols:
		globals()[symbol] = getattr(module, symbol)

	__all__.extend(public_symbols)
