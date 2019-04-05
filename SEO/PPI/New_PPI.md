This PPI calculator (pixels per inch calculator) finds the resolution of your display based on its dimensions and the pixel count. We will teach you what is PPI, we'll explore the differences between PPI vs DPI through the DPI defintion as well as some comments on the dot pitch definition and fall out of use. Of course this is a calculator so we'll show you how to calculate PPI and how to categorize resolution based on PPI.

## PPI definition: What is PPI?

PPI is an acronym widely spread around the tech forums of the Internet, specially those focused on display technology and smartphones. It stands for Pixels Per Inch, and it represents a measurement of the pixel density of a screen or a digital image. The <portal cid=204>density</portal> is measured as the number of pixel that fit in a line of size 1 inch, hence the name. 

This measurement is based on the fact that screens and images, despite being 2D, have generally the same density along any of the two main directions. The are other measurements of pixels density such as pixel per square inch, that involve calculating the <portal cid=749>area of a rectangle</portal> that is the screen. Also worth mentioning is the fact that our pixel density calculator assumes <portal cid=173>square</portal> pixels. 

It is important to note that for calculating PPI we need something that has a physical size, not a virtual file. For example, a screen or a printed picture have a fixed physical size so it makes sense to talk about their PPI. However, when we're talking about a digital image in a computer PPI cannot be computed since the digital image varies in size depending on the level of zoom, the size of the screen... For purely virtual images we have a calculator, though, that allows you to convert between different virtual sizes: <portal cid=323>px to em calculator</portal>

## How to calculate PPI, the theory

You can calculate PPI in multiple ways. The most common one is to calculate it from the diagonal screen size (in inches or cm) and the amount of pixels along the vertical and horizontal edge of the display.

First, you need to calculate the number of pixels that fit on the diagonal:

`dₒ = √(w² + h²)`

where

* **w** is the number of pixels along the horizontal, and
* **h** is the number of pixels along the vertical. 

Then, you can calculate the PPI as the ratio between the number of pixels along the diagonal and the diagonal screen size:

`PPI = dₒ/dᵢ`

where **dᵢ** is the diagonal screen size in inches.

You probably noticed that you can also enter the width and height of the display into the PPI calculator. You can use these values instead of the diagonal size of the screen. Remember, though, that the <portal cid="300">aspect ratio</portal> must be the same both for the size expressed in inches and pixels. 

Our pixel density calculator also finds the total number of pixels on the display, expressed in megapixels (millions of pixels, symbol: Mpx). This value is found as the product of the vertical and horizontal amount of pixels.

## Dot pitch definition

The last number that you can find with our calculator is the dot pitch - the distance between two pixels' centres. This is calculated as the inverse of PPI. If PPI is a measure of the density of pixels in a given length, dot pitch is the exact opposite: is the distance between two fixed pixels or dots. Note that we are using dots and pixels interchangeably but this might not always be the case.

The dot pitch is somewhat forgotten and the dot pitch value is mostly not used due to the advancements of modern technology. Back in the days when smartphones (and even computer monitors) had resolutions of less than 100pixels in both vertical and horizontal directions, the usage of dot pitch was convenient and understandable. 

Now, however, our devices have couple thousands of pixels in less than 5inches making the dot pitch values ridiculously small and hard to understand intuitively. This means was the doom of dot pitch but the upraise of PPI as the new de-facto standard. And that's the reason dot pitch is fading out of the mainstream scene and why most people don't know what the dot pitch definition is.

Before we move to an example use case of the calculator, we must mention DPI. DPI, or Dots Per Inch is a similar measurement to PPI as they both measure density. However, they do it in subtly different ways, or at least they used to.

## DPI definition, dots per inch definition

DPI is, as we mentioned before, "Dots per inch" and it's analogous to PPI in the sense that they both measure how "grainy" an image is. As the name suggest, dots per inch measures the number of points that exist in the <portal cid=208>length</portal> equivalent to `1 inch` on average. This value is directly related to PPI for modern digital screens since each pixel corresponds to a dot in the image, but it doesn't always have to be a 1:1 correlation.

If you think of an ink printer, their settings usually include DPI, and not PPI. This is because, in a printer, DPI means the number of ink dots per inch, and it's independent of the resolution of the image we want to print. Depending on the printer's characteristics its DPI can be higher or lower than the PPI of the image we want to print. Let us illustrate with an example.

Assume you have a printer capable of up to 300dpi when printing. Imagine you have a `1800x2800 ~ 5 Mpx` picture that you want to print into a paper with an actual size of about 6 inches measured in the diagonal. The pixel density of the image at this size is 554.8 ppi, way higher than the 300dpi your printer is capable of. In this case each ink dot printed will represent several pixels of the image, so we will lose resolution in the printing process.

If we imagine the same scenario but better printer capable of 1000dpi the scenario reverses. In this situation each pixel will be composed of several dots of ink. A general recommendation is to set the DPI in the printer to an integer fraction or multiple of the original pixel density of the image, to avoid the kinds of artefacts that appear when interpolating pixels and guessing color values.


## Using the pixels per inch calculator: an example

Let's assume you want to calculate the PPI of your smartphone.

1. Check what is the diagonal size of your smartphone. Let's say it is equal to 5 inches.
2. Write down the vertical and horizontal pixel count. Let's assume they are equal 640 and 480 pixels respectively.
3. Calculate the amount of pixels along the diagonal: 

`dₒ = √(w² + h²) = √(480² + 640²) = √640,000 = 800`

4. Calculate the PPI according to the formula written above:

`PPI = dₒ/dᵢ = 800/5 = 160`

5. The total count of pixels is found as the product of **w** and **h**:

`w * h = 480 * 640 = 307,200 = 0.307 Mpx`

6. Calculate the dot pitch as the reciprocal of PPI:

`dot pitch = 1/160 in = 0.00625 in = 0.1588 mm`


## PPI vs DPI: the differences

When we are talking about screen densities, two values pop-up: DPI and PPI. DPI stand for dot per inch, while PPI is the same about pixels. The differences when talking about screens are none, since the pixel is considered the "dot" of a screen. Things are a bit more complicated when we compare PPI vs DPI outside of screens, or when we consider the comparison at a deeper level. 

We have mention the differences of PPI vs DPI when we are talking outside of screens like, for example, when printing an image on paper. This arises from the distinction between dot and pixel (which is the equivalent in digital form). If we stay in the purely virtual realm of digital technology a pixel, being the minimal unit of digital space, is exactly the same as the dot.

However, in the physical-digital world, things become more complicated. A screen is a physical object that connects the virtual-digital world with our analogical-physical perception of reality. In a screen a pixel is not actually one dot but it is composed of 3 individual dots of different colors, namely red, green and blue. This is where the similarities between pixel and dot start to break down a little and it makes sense again to compare PPI vs DPI.

This is especially noticeable when we encounter pentile matrix screens. In these screen the three colors that make up one pixel are not the same size and the perceived resolution ends up being smaller. In this cases one can make a distinction between PPI vs DPI that really matters and that goes beyond pure semantics.

## Does (PPI) size matter?

Oh, the age old question! Is bigger better? Such a common question requires a similarly old and used answer: <strike>HELL YES!</strike>**"it depends"**. Jokes aside, having a higher PPI or DPI is in general better since it means having a finer image that retains a greater amount of details. However, there's always **a trade of and there are certain scenarios in which having a higher PPI count might be detrimental**.

If we have a small screen, such as those in our smartphones, or if we look at and image from far away (like a TV or a cinema projector) there's a **point at which our eyes are not able to detect each individual pixel** and increasing the PPI has a smaller and smaller effect. This is the principle behind the so-called "Retina display" that Apple uses in their devices. 

This threshold **depends on the distance** at which we typically look at the screen, as well as the size of the screen. For example, the iPhone XR PPI is 326 while the iMac with a 5K screen has 218ppi. The iPhone XR PPI count is clearly higher since we tend to **look at our smartphones much closer** that we (should) look at a computer monitor. 

A second situation in which bigger might not be better is when we are mixing resolutions between the source and the display/printer. We already mentioned the printing problem, but we might encounter a similar issue when dealing with photos or videos online. The best case scenario is to have the highest resolution possible and matched 1:1 between the source and the monitor we watch it in. 

If that's not possible, then finding one resolution to be integer multiple/fractions of the monitor is the second best option since that would allow for direct mapping of pixels and avoid weird interpolations. If that's also not possible, the best option is to match aspect ratios. But notice that all those geometrical parameters are more important than raw resolution.

So, even though bigger PPI is generally better, **it really depends**, as we saw when comparing the iPhone XR PPI vs the iMac

## How many pixels per inch is a normal PPI value?

You might be wondering, after all this calculations and definitions, if your monitor / smartphone /... Has a good density of pixels. If your phone or monitor was made in the last 3 years, we can almost guarantee that they have a respectable number of pixels per inch. However, if you want to have a more objective and precise reference, here we have a list of what is considered high, low, and medium pixels per inch. Just remember that as technology evolves, we see less of the lower end and more of the high end, and we will possibly get even higher values just for the sake of marketing.

The list below presents the categories of pixel density - from the lowest to highest quality.

* LDPI: Low density, 120 PPI
* MDPI: Medium density, 120-160 PPI
* TVDPI: Medium High density, 160-213 PPI
* HDPI or HiDPI: High density, 213-240 PPI
* XHDPI: eXtra High density, 240-320 PPI
* XXHDPI: eXtra eXtra High density, 320-480 PPI
* XXXHDPI: eXtra eXtra eXtra High density, 480-640 PPI
