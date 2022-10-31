import lib.glowbit as glowbit

matrix_display = glowbit.matrix8x8(pin=12)

# sensor display constants - driven by position on case for display/UI
OXYGEN    = 0
LIGHT     = 1
NOISE     = 2
CO2       = 3
TVOC      = 4
TEMP      = 5
HUMIDITY  = 6
PRESSURE  = 7

oxygen    = matrix_display.graph1D(originX=0, originY=0, length=8, minValue=0, maxValue=8, direction="Right")
light     = matrix_display.graph1D(originX=0, originY=1, length=8, minValue=0, maxValue=8, direction="Right")
noise     = matrix_display.graph1D(originX=0, originY=2, length=8, minValue=0, maxValue=8, direction="Right")
co2       = matrix_display.graph1D(originX=0, originY=3, length=8, minValue=0, maxValue=8, direction="Right")
temp      = matrix_display.graph1D(originX=0, originY=4, length=8, minValue=0, maxValue=8, direction="Right")
humidity  = matrix_display.graph1D(originX=0, originY=5, length=8, minValue=0, maxValue=8, direction="Right")
tvoc      = matrix_display.graph1D(originX=0, originY=6, length=8, minValue=0, maxValue=8, direction="Right")
pres      = matrix_display.graph1D(originX=0, originY=7, length=8, minValue=0, maxValue=8, direction="Right")

def update_display(*sensor_values):
    '''
        accepts list of length 0 or more tuples:
            [('SENSOR', value), ...]
            where sensor refers to list of sensor ID constants above
            and value is safety value on interval [1,8]
    '''
    # print(f"updating display: {sensor_values}")
    for sensor, value in sensor_values:
        if value < 1 or value > 8:
            return #error (raise exception? or just skip?)
        elif sensor == 'oxygen':
            # print(f"updating display for OXYGEN:::")
            # matrix_display.updateGraph1D(oxygen, 5)
            matrix_display.updateGraph1D(oxygen, value)
        elif sensor == 'light':
            matrix_display.updateGraph1D(light , value)
        elif sensor == 'noise':
            matrix_display.updateGraph1D(noise , value)
        elif sensor == 'co2':
            matrix_display.updateGraph1D(co2 , value)
        elif sensor == 'tvoc':
            matrix_display.updateGraph1D(tvoc , value)
        elif sensor == 'temp':
            matrix_display.updateGraph1D(temp , value)
        elif sensor == 'humidity':
            matrix_display.updateGraph1D(humidity , value)
        elif sensor == 'pressure':
            matrix_display.updateGraph1D(pres , value)
        else:
            return
    matrix_display.pixelsShow()

def startup_fireworks():
    matrix_display.fireworks()

def debug_set_pixel(x, y):
    matrix_display.pixelSetXY(x, y, matrix_display.white())
    matrix_display.pixelsShow()