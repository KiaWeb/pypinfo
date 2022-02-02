# pypinfo
THIS DOES NOT WORK IN PIP. Simply download pinfo.py and import it into any of your scripts.
Remember, BSD license. Give credit to me using `Github/KiaWeb`.
# Tutorial
- Download the source code's .zip file.
- Put the pinfo.py into the directory of your python script.
- Simply `import pinfo`.
- Type `pinfo.infocreate(name, author, date, version, filename)`. Make sure `filename` does not have an extension, pinfo only searches for .pinfo files.
- OR, you can type `pinfo.setup()`, and it'll ask you.
# WARNING: Do NOT type `pinfo.start_main(fn)` or else it won't put info inside. Just `pinfo.setup()` and `pinfo.infocreate()`.
- Kia
