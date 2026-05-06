# VDF2 - Python VDF parser
## Installation:
`pip install vdf2`

## Usage:
### With strings
`vdf2.loads("string") # -> dict object`
`vdf2.dumps(dictionary) # -> vdf string`

### With IOStreams
`vdf2.loads(file) # -> dict object`
`vdf2.dumps("vdf contents", file) # -> saves vdf into file`
