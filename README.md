## **Canary** :baby_chick:
### *Safety and environmental monitoring device*
&nbsp;
### Balena Labs residency project

&nbsp;
---

<figure>
    <img src="img/canary_image_1.png" height="500" />
    <figcaption>Canary environment monitor</figcaption>
</figure>

&nbsp;

### Motivation and objectives

---

The main purpose of this project was to attempt to experience a 'day (month) in the life' of a product builder or entrepreneur who wanted to rapidly prototype a device which they have an idea for.

Taking inspiration from my experience working in industrial settings and around the house I decided to put together a small device which can be taken into a work environment and provide basic feedback about the potential safety hazards present.

Essentially I wanted to see how difficult it would be to take a collection of inexpensive sensors and compile them into a tangible product. It was more about the journey than the destination.

The finished product is not intended to be a be-all and end-all device, but more of an exemplary project of how one might attempt to realise an idea in a short period of time.

&nbsp;

### Initial Concept

---

The following are some environment variables which should be observed in a work place:
- Noise
- Oxygen (especially in enclosed spaces, and when welding)
- Light (it's often easy to persist with inadequate light but having a measure is helpful)
- Voltile Compounds which may have adverse health effects
- Temperature (if nothing other than a reminder to stay hydrated)


With these variables in mind, a selection of sensors were assembled:`

[ADAFRUIT SGP30 AIR QUALITY SENSOR](https://www.adafruit.com/product/3709):
- CO2 (parts per million)
- TVOC (parts per billion)

[GRAVITY: I2C OXYGEN SENSOR](https://www.dfrobot.com/product-2052.html):
- O2 (percentage of environmental air composition)

[BH1750FVI DIGITAL LIGHT INTENSITY SENSOR](https://core-electronics.com.au/bh1750fvi-digital-light-intensity-sensor-module-gy-302.html):
- Light level sample (lux)

[PIICODEV ATMOSPHERIC SENSOR BME280](https://core-electronics.com.au/piicodev-atmospheric-sensor-bme280.html):
- Temperature (℃)
- Relative Humidity (%)
- Atmospheric Pressure (Pa)

[SEN-12642 SOUND DETECTOR](https://www.sparkfun.com/products/12642) which also required an [Analogue To Digital Converter](https://www.adafruit.com/product/856):
- Sound volume indication (more [here](https://learn.sparkfun.com/tutorials/sound-detector-hookup-guide))

So we cover the variables above and get some bonus metrics which will be included for good measure.

Fortunately I happened to have a Raspberry Pi 3B model at home, which is suitable to use for the main compute/control functionality.

&nbsp;

### Putting it together - Hardware

---

Various ideas come to mind when thinking about a device which accompanies one in the workshop environment. 

Ultimately the guiding motivation was to make it as simple as possible. This is after all a one month project and the aim is to learn and explore. 

Simple solution: for each variable listed above, display it's safety value on a panel of LEDs.

In essence, the user needs to be able to glance at the device and quickly realise 'oh I'd better use breathing protection/employ ventilation system because the air quality is poor' or 'yes it is justified to seek an alternative light source because the light levels are too low', or 'yes, I should remove small children from this environment in the interest of not damaging their hearing'.

&nbsp;
<figure>
    <img src="img/canary_image_6.png" height="500" />
    <figcaption>some initial sketches</figcaption>
</figure>
&nbsp;
<figure>
    <img src="img/canary_image_2.png" height="500" />
    <figcaption>putting together the components</figcaption>
</figure>
&nbsp;
<figure>
    <img src="img/canary_image_3.png" height="500" />
    <figcaption>more testing</figcaption>
</figure>
&nbsp;
<figure>
    <img src="img/canary_image_4.png" height="500" />
    <figcaption>checking the measurements</figcaption>
</figure>

Once the design was paired back a little, a simple 3D printed case was devised, with allowances for the LEDs, light sensor and mounting points for our Raspberry Pi. 


So we have sensors inside a case, with LED matrix display for user signalling/feedback, connecting to a Raspberry Pi.


Your author, being inexperienced with hardware assembly mistakenly decided to attempt to solder together rows of 8x LEDs. 

Upon accepting the limitations of my soldering ability, I decided to instead opt for an 8x8 matrix LED module which was much easier to integrate.

The [glowbit 8x8 Matrix LED](https://core-electronics.com.au/glowbit-matrix-8x8.html) module was selected, as it comes with a nice software library to control and didn't need any additional resistors or componentry to assemble. 

<figure>
    <img src="img/header.gif" height="500" />
    <figcaption>LED matrix integrated with case</figcaption>
</figure>

&nbsp;

### Putting it together - Software

---

Once everything was assembled, I started conducting some simple tests using the Python libraries provided by each OEM. 

Speaking as someone who has not really tinkered with sensors and hardware on this level before, it was surprisingly easy to get up to speed with the concepts (I2C addressing, Raspberry Pi GPIO) and this project once again reiterated to me the low barrier to entry Python enables.

Thanks to the internet, I found some information about appropriate settings for sensor safety values and mapped this to the 1-8 display scale provided by the LED matrix. (Not a perfect solution, but enough for a proof of concept).

&nbsp;
<figure>
    <img src="img/canary_image_1.png" height="500" />
    <figcaption>Canary environment monitor</figcaption>
</figure>
&nbsp;

### Improvements
 
---
 
In hindsight, it's clear that the optimal user feedback is not a bar graph of LEDs, especially when different sensors have different intuitive values. So it's obvious that a screen of some sort would greatly improve this device. This would also address the resolution issue with debossed text seen in the image above.

Perhaps a solution might be some sort of device-phone interaction.

Finally, once the device design is mature, the design can be scaled to a fleet of devices. These could be installed in various locations throughout a workshop to monitor conditions, to help improve workshop layout and equipment placement.

&nbsp;

---
