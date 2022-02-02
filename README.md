# morningwhale

*keen* (noun): a mourning wail


## architecture (intent)
three layers, starting with the most private:
- elasticsearch, fully encapsulated/hidden by:
- `morningwhale` (aka `mw`), a very trusting logging service that is available to the internet only through:
- a yet-to-be-decided public analytics api that will protect `mw` from all harm
