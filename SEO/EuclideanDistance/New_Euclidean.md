# LEAD


## What is distance?

Before we get to how to calculate distances, we should probably clarify what distance is. In the most typical meaning of distance it is the 1D space between two objects. This definition is one way to say what almost all of us think of distance intuitively, but it is not the only way we could talk about distance. You will see in following sections how the concept of distance can be extended beyond <portal cid=208>length</portal>. In fact, in more than one sense, that is the breakthrough behind Einstein's theory of <portal cid=751>relativity</portal>.

If we stick with the geometrical definition of distance we still have to precise what kind of space we are working on. In most cases you are probably talking about 3 dimensions or less, since that's all we can imagine without our brains exploding. For this calculator we will focus only on the 2D distance (with the 1D included as a special case). If you are looking for the 3D distance between 2 points we invite you to use our <portal cid=291>3D distance calculator</portal> made specifically for that purpose. 

To determine the distance between two point, the first thing you need are two points, obviously. These points are described in mathematics by their coordinates in space. For each point in 2D space we need 2 coordinates. These two coordinates are unique to this point. If you wish to find the distance between two point in 1D space you can still use this calculator by simply setting one of the coordinates to be the same for both points. Since this is a very special case, from now on we will talk about distance meaning "_2D distance_".

Next step to do, if you want to be mathematical accurate and precise, is define the type of space you're working on. No, wait, don't run away! It is easier than you think. If you don't know what space you're working on or if you didn't even know there was more than one type of space, you're most likely working in Euclidean space. Since this is the "default" space in which we do almost every geometrical operations, it is the one we have set for the calculator to operate on. Let's dive a bit deeper into Euclidean spaces, what they are, what properties they have and why are so important.


## The distance formula for Euclidean distance

The Euclidean space or Euclidean geometry is precisely what we all think of space of geometry before we receive any deep mathematical training in any of these aspects. In Euclidean space the sum of <portal cid=1111>triangle angles</portal> is 180º. <portal cid=1085>Squares</portal> have all their angles equal to 90º, always... Which is something we all take for granted, but that is not true in all spaces.  Let's also not confuse Euclidean space with multidimensional spaces. Euclidean space can have as many dimensions as you want and still be Euclidean. 

We do not want to bore you with mathematical definitions of what a "_space_" is and what makes the Euclidean space unique, since that would be too complicated to explain in a simple distance calculator. However we can try to give some examples of other spaces that are commonly used and that might help you understand why Euclidean space is not the only space. Also you will hopefully understand why we are no going to bother calculating distances in other spaces.

The first example we present to you in a bit obscure, but I hope you can excuse myself as a physicist for starting with this very important type of space: "_Minkowski space_". The reason I've selected this is because it is highly used in physics, in particular in relativity theory, general relativity and even in relativistic quantum field theory. This space is very similar to Euclidean space, but differs from it in a very critical feature: <portal cid=560>dot product</portal>, also called the _inner product_ (not to be confused with the <portal cid=561>cross product</portal>). 

Both the Euclidean and Minkowski space that we have talked about are what mathematicians call flat space. This means that space itself has flat properties; for example the shortest distance between any two points is always a straight line between them (check the <portal cid=486>linear interpolation</portal> calculator). There are, however, other types of mathematical spaces called "_Curved spaces_" in which space is intrinsically curved and the shortest distance between two points is no a straight line.

This curved space is hard to imagine in 3D but for 2D we can imagine that instead of having a flat plane <portal cid=210>area</portal> we have a 2D space curved in the shape of, for example, the <portal cid=475>surface</portal> of a <portal cid=1067>sphere</portal>. In this case, very strange things happen. For example, the shortest distance from one point to another is not a straight line, because any line in this space is curved due to the intrinsic curvature of the space. Another very strange feature of this space is that some <portal cid=704>parallel lines</portal> do actually meet at some point. You can understand this better by think of the so called "parallels" that divide earth in many <portal cid=1141>time zones</portal> and cross each other at the poles.

It is important to note that this is conceptually VERY different from a change of coordinates. When we take the standard `x, y, z` coordinates and convert into <portal cid=552>polar coordinates</portal>, or <portal cid=554>cylindrical coordinates</portal>, or even <portal cid=555>spherical coordinates</portal> but we will still be in Euclidean space. When we talk about curved space we are talking about a very different space in terms of it intrinsic properties. In spherical coordinates you can still have a straight line and distance is measured in a straight line, even if that would be very hard to express in numbers. 

Coming back to the Euclidean space we can now present you with distance formula that we promised at the beginning. The distance formula is `√(x₂ - x₁)² + (y₂ - y₁)²`, which relates to the <portal cid=53>Pythagorean theorem</portal>, which is `a² + b² = c²`, where `a` and `b` are legs of a right triangle and `c` is the hypotenuse. Suppose (x₁,y₁) and (x₂,y₂)are coordinates of the endpoints of the hypotenuse. Then `(x₂ - x₁)²` in the distance equation corresponds to `a²` and `(y₂ - y₁)²`corresponds to `b²`. Since `c = √a² + b²`, you can see how it is just an extension of the Pythagorean theorem.

## Distance from a straight like or any continuous structure

The distance formula we have just seen is the standard Euclidean distance formula, but if you think about it, it can seem a bit limited. Not always we would want to calculate the distance between too points, sometimes we want to calculate the distance from a point to a line, or to a <portal cid=752>circle</portal>... In this case we first need to define what point in this line or <portal cid=288>circumference</portal> we will use for the calculation, and then use the distance formula that we have seen just above.

Here is when the concept of <portal cid=<portal cid=700>perpendicular line</portal> becomes of crucial importance. The distance between a point and a continuous object is defined via perpendicularity. From a geometrical point of view the steps to be taken to measure distance from one point to another is to create a straight line between both points and then measure the length of that segment. When we measure the distance from a point to a line, the question becomes "Which of the many possible lines should I draw?" in this case the answer is: **the one line that includes the point and is prependicular to the first line** from which we want to measure the distance to the point. In the case that the point would be part of the line, the distance would be zero. For these 1D cases, one can only consider distance between points, since the line represents the whole 1D space. 

Apart from perpendicularity, another important concept to talk about regarding distance is the <portal cid=239>midpoint</portal>. This is the point that is precisely in the middle between two. The midpoint is defined as the point that is the same distance away from each of the points of reference. We can and will generalise this concept in a later section, but for now we can limit ourselves to geometry. For example the mid point of any diameter in a <portal cid=753>circle</portal> or even a <portal cid=896>sphere</portal> is always the centre of said object.

## How to find the distance from one point to another using our distance calculator

As we have mentioned before, distance can mean many things but we focused this calculator on obtaining the distance between two points in 2-D space.  In 2-D space points are defined by two coordinates each, and that's why the distance calculator here has four text boxes for you to fill-in. Using the calculator is very straight-forward, but before you use it, we would recommend you to get acquainted with the distance formula and the procedure you would have to follow if it was 1950 and the Internet was still not a thing.

Suppose we have coordinates `(3,5) and (9,15)` and we want to calculate the distance. These would be the steps your should take to calculate the 2-D distance between these two points:

1. Input the values into the formula: `√(x₂ - x₁)² + (y₂ - y₁)²`.
1. Subtract values in parentheses.
1. Square both quantities in parentheses.
1. Add the results.
1. Take the <portal cid="151">square root</portal>.
1. Use the distance equation to check results.

Working the example by hand, we get `√(9-3)²+(15-5)²` = `√36 + 100` = `√136`, which is approximately equal to 11.66.  Note that when taking the square root you will get a positive and negative value, but since we are dealing with distance, we are only concerned with the positive result. 

## Driving distance between cities: a real world example (to be checked and expanded)

An application of the distance calculator is that is can be used together with the <portal cid="30">gas calculator</portal>. 

Suppose you are traveling from city A to city B and the only reference is city C, with route A to B perpendicular to route B to C. We can determine the distance from A to B. From this the gas calculator will determine fuel cost, fuel used and cost per person while traveling. 

Another common calculation used with line segments is calculating the midpoint. The is important when determining segment bisectors in geometric proofs and constructions. Calculating the midpoint involves coordinates (x₁,y₁) and (x₂,y₂), as does the distance calculator and is done simply with the <portal cid="239">midpoint calculator</portal>

The more complex version of the distance formula can be used to find <portal cid="291">the distance between coordinates in a three-dimensional coordinate system</portal>. The formula involves coordinates (x₁,y₁,z₁) and (x₂,y₂.z₂) and is √(x₂ - x₁)² + (y₂ - y₁)² +(z₂ - z₁)².

## Distance from Earth to Moon and Sun, and astronomical distances



## Distance beyond length

