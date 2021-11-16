Hey, this is lib can like this:

```python
from pyndustry.pyndustry import *

storage = CommandsStorage()
Mprint('Hello world!', 'message1')
storage.convert()
```

Output:
```mindustry
printflush message1
print "Hello world!"
```



and like this:
```python
from pyndustry.pyndustry import *
from pyndustry.memory import *

storage = CommandsStorage()
mem = MemoryStorage('cell1')
Mif(mem[0] > 10,
	Function(lambda :
		Mprint('Wow', 'message1'))) \
.apply()
End()
storage.convert()
```

Output:
```mindustry
read memoryStorageResult__cell1 cell1 0
jump 3 greaterThan memoryStorageResult__cell1 10
jump 5 always x false
printflush message1
print "Wow"
end
```


and 
```python
from pyndustry.pyndustry import *
from pyndustry.graphics import *

storage = CommandsStorage()
display = Display('display1')
display.bind()
display.drawGameSprite(0.5, 0.5, sprites.blocks.router, 16, byCoefficient=True)
storage.convert()
```

Output:
```mindustry
drawflush display1
draw image 40.0 40.0 @router 16 0 0
```