Simple QT gui to generate a png annotated image of a quantum device annotated with instrument values.

Simple use case:

```python
from qcodes_device_annotator import DeviceImage
di = DeviceImage('.', station)
di.annotateImage()
di.updateValues(station)
counter = 0
di.makePNG(counter)
```
