### language

A set of strings.

Examples
```
a*b*c*
a+b?
```

### grammar

The description of a language.

Examples
```
abc
aadbcc
b
''
ccccc
```

## Describing Grammar

Since grammar can be difficult to explain using examples alone, we 
define an API so that we describe a series of function calls

| Name    | Function  | Example use | Example Out   |
|-------- |:---------:| -----------:|:--------------|
| Literal | `lit(s)`  | `lit('a')`   |  `{a}`       |
| Sequence| `seq(x,y)`| `seq(lit('a'), lit('b'))` | `{a,b}` |
| Alternatives | `alt(x,y)`| `alt(lit('a'), lit('b'))` |  `{a,b}` |
| Any number of reps | `star(x)` | `star(lit('a'))` | `{",a,aa,aaa,...}` |
| One of | `oneof(c)` | `oneof('abc')` | `{a,b,c}` |
| End of line | `eol` | `seq(lit('a'),eol)`| `{"}`, `{a}` | 
| Match any character | `dot` | `dot`  | `{a,b,c,...}` |

