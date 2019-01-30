## Vector cross product definition

A vector is a mathematical tool, widely used in physics, that allows you to deal with collections of numbers (dimensions) in a very efficient way. The collection of operations, rules and properties to deal with vectors is called vector algebra and, similarly to the algebra of numbers, it includes multiplication operations. However, operations with vectors are more complex than with numbers since they carry much more information that has to be carefully manipulated. This is one of the reasons why in vector algebra there are two different types of multiplications or product operations: the cross product and the <portal cid=560>dot product</portal>.

The definition, as it is common with mathematical stuff, is very technical but we will explain you what it means in more normal (and less accurate) terms so that even if you don't have a strong mathematical background everything will make sense for you. According to <a href=https://en.wikipedia.org/wiki/Cross_product>Wikipedia</a> the cross product, also called _vector product_ is: 

`Is a binary operation on two vectors in three-dimensional space and is denoted by the symbol ×. Given two linearly independent vectors **a** and **b** the cross product, **a × b**, is a vector that is perpendicular to both **a** and **b** and thus normal to the plane containing them.`

That is indeed a mouthful but we can translate from mathematical jargon into everyday explanation so that we can all understand it. First of all the definition talks about a three-dimensional space, like the one we live in, because it is the most common usage of the cross product, but the cross product can be extended to more dimensions; that is, however, beyond the scope of this text and most math-related degrees. 

What the definition is telling us is that the vector cross product of any two vectors is a third vector that is <portal cid=700>perpendicular</portal> to both of them (and to the plane that contains them). This is possible in 3-dimensional space because in such a space there are 3 independent directions. To put it in everyday terms, you can think of these three directions as being height, width and depth.

To know how this new third vector will look like in terms of size, and mathematical description, we will use the formula for the cross product of two vectors. In the next section you will be presented with the formal, mathematical formula that tells you how to do the cross product of any two vectors. As we also do at Omni, we will also explain what this equation means and how to use it in a simple, yet accurate way.

## Cross product formula

Before we present to you the formula for the vector product we need two vectors that we will call `a` and `b`. These two vectors should not be collinear (a.k.[. parallel) for reason that we will explain after we see the formula. We will call the resulting vector from the cross product formula `c`. We also remind you that the letter `n` is used to denote a <portal cid=553>unit vector</portal>(perpendicular to both `a` and `b`. So without further ado let's see the formula:

`c = a × b = |a| * |b| * sinθ * n`,

According to this formula, the resulting vector `c` from performing the cross product between `a` and `b` is a vector perpendicular to both (that's where the `n` part of the equation comes in). The modulus/norm/length of this new vector is equal to the "normal" product of the modulus of each of the initial vectors times the sinus of the angle between them (`θ`). The fact that there is a factor of perpendicularity, together with the fact that we have a sinus function in the formula are good indicators of the geometrical interpretations of the vector cross product. We will more about those when we explain the properties of this mathematical operation.

You can also see in the formula why it is important that the two vectors `a` and `b` not be parallel. If they where parallel that would mean that the angle between both of them will be `θ = 0` and hence we will have both `sinθ = 0` and `c = 0` which is a very uninteresting result. This leads, however, into another use for the vector cross product which we will explain later.

## How to do the cross product of two vectors

We have seen the mathematical formula for the vector cross product, but you might still be thinking "_This is all well and good but how do I **actually** calculate the new vector?_" And that is a very good question. By far the fastest and easiest solution is to use our vector cross product calculator, but if you have read this far you are probably looking not only for results but also for knowledge, so we'll give it to you. We will divide the process into 3 different steps: calculating the modulus of a vector, calculating the angle between two vectors, and calculating the perpendicular unitary vector. Putting all these three intermediary results together by means of a simple multiplication will yield the desired vector.

However, calculating angles between vectors might get too complicated in 3-D space if all we want to do is to compute the cross product between two vectors. So let's explore a simpler, more efficient and practical way of calculating the vector cross product by means of a different cross product formula. This new formula makes use of the decomposition of a 3D vector into its 3 components. This is a very common way to describe and operate with vectors in which each component represents a direction in space and the number accompanying it represents the length of the vector in such direction. Cannonically the three dimensions of the 3-D space we're working with are named `x`, `y` and `z` and are represented by the unitary vectors **i**, **j** and **k** respectively.

Following this nomenclature each vector can be represented by a sum of these three unitary vectors. The vectors are generally omitted for brevity but are still implied and have a big bearing on the result of the cross product. So a vector **v** can be expressed as: `v = (3i + 4j + 1k)` or in short: `v = (3, 4, 1)` where the position of the numbers matters. Using this notation we can now see and understand a very easy way to calculate the cross product of two vector, which we will call `v = (v₁, v₂, v₃)` and `w = (w₁, w₂, w₃)`. For these two vectors the formula looks like:

`v x w = ( v₂w₃ - v₂w₃,  v₃w₁ - v₁w₃, v₁w₂ - v₂w₁)`

<later>This result might look like a random collection of operations between components of each vector, but nothing is further from reality. For those of you wondering where this all comes from we encourage you to try and discover it yourself. All you need to do is start with both vectors expressed as: `v = v₁i + v₂j + v₃k` and `w = w₁i + w₂j + w₃k` and multiply each component of a vector with all the components with the other. As a small help or hint we can tell you that when doing the cross product of vectors multiplied by numbers the result is the regular product of the numbers times the cross product between vectors, as we will see in the next section. It will also come in handy to remember that the cross product of parallel vectors (and hence of a vector with itself) is always `0` as we've seen before.

For starters let's tackle obtaining the modulus, norm or length of a 3-D vector. For that we simply need to calculate the <portal cid=291>3d distance</portal> from the beginning to the end of the vector. That can be done using our calculator or by simply taking each of the three components, squaring them, summing them and the performing the <portal cid=151> square root</portal> of the result. Putting it in mathematical terms (using vector `a`) as an example we get:

`|a| = √(a₁² + a₂² + a₃²)`

Where `a₁`, `a₂` and `a₃` represent each of the components of the 3d vector `a`.  </later>

## Cross product properties


## How to use the vector cross product calculator

So after all the things we've talked about it's time to get to know how to use our cross product calculator to save time and obtain results for any to vectors in 3-D space. As you can see, the variables are devided into 3 sections, one for each vector involved in a cross product calculation. Of these three vectors `c` is probably the one you should care about the most since it is the result of the cross product of the other two vectors `a` and `b`. Each vector has 3 components as mentioned before: `x`, `y` and `z` referring to the each of the three dimensions (depth, width and height).  

Once we have understood what each of the field does, let's take a quick look at a normal use case for this calculator. To include an example for calculating the cross product of two vectors, we will use the vectors: `a = (2, 3, 7)` and `b = (1, 2, 4)`. 

1) First step is introduce the components of vector `a`. That is: `x=2`, `y=3` and `z=7`
1) Next you should introduce the components of vector `b`. That is: `x=1`, `y=2` and `z=4`
1) _Voilà!_ you have just calculated `c = a x b = (-2, -1, 1)`
1) Repeat again until you have calculated all the cross products you needed to
1) Share with your friends the life changing experience of calculating vector cross products. ;)

You can calculate the cross product of any vectors you want, without even having to think about it. However we highly recommend you to use the properties we have mentioned above for complex operations to save you time and hassle. For example if one of the vector is simply a multiple of the other you don't even need to use our calculator, you can just simply know that the result will be zero since those to vectors are collinear.

## Dot product vs cross product

We have explored most of the mathematical aspects of the cross product of two vectors in 3-D space, so it's time to talk about some interesting facts and uses of this vector operation. To kick things off we will talk about the _cousin_ of the cross product: the dot product. This two operations have a misleadingly close name but in fact represent different concepts in mathematics and geometry. On top of that computing the dot product is arguably easier than computing the cross product; nevertheless we have also made a calculator to help you calculate the <portal cid=560>dot product of 2 vectors</portal>, also called the scalar product.

Keeping up with the trend of apparent similarities between the scalar product and the cross product we can take a close look at the formula for the dot product:
`v = a · b = |a|*|b|*cosθ`
where the only differences between the cross product and the dot product are the trigonometric function and the fact that the result is a number (scalar, hence the name) rather than a vector as it was the case with the cross product.

These small difference might have you believe that both operations are very similar but they are very different in nature. For starters, the cross product is an operation that takes two vectors and returns another vector perpendicular to both, while the dot product returns a number with no direction. The dot product is also much more easily generalizable to higher or lower dimensions, while the cross product does not even exist in 2-D. Their interpretation in geometrical terms is also very different since you can think of the dot product as the length of the projection of one of the vectors onto the other.

All those differences make them very distinct operations conceptually and are, therefore, not interchangeable or translatable. Both operations are very useful in both mathematics and physics as we will see in the following sections.

## Cross product and physics: Best Friends Forever

As always, most of us are not interested just in the purely mathematical properties and uses of the cross product but also in the practical application in the real world. And what better way to get a useful application of mathematical concepts than through physics. The cross product is not an exception and it is a very useful operation in physics. We could get deep into Quantum Field Theory where both the scalar product and the cross product are widely used. However we will stay within the realm of tangible and mathematically perfect theories and look at examples in places and events we can all relate to. 

The first field in which the cross product properties are widely used is electromagnetism. In nature, electric and magnetic fields are generally present perpendicular to each other, which ties perfectly into the way the cross product of two vector is expressed. Thing like calculating the <portal cid=903>magnetic forces on a current-carrying wire</portal> or computations for the <portal cid=970>magnetic moment</portal> of a system, all require the use of the cross product operation. Another example that cannot go unmentioned is the so called <portal cid=1050>Hall effect</portal> that is a very important effect in solid state physics but whose explanation is far too complicated to be treated here, so we invite you to visit the calculator we made for such effect.

`Walter Lewin on moment of inertia => chair+wheel`

An even more tangible place where we can use the cross product formula to predict things is when we talk about <portal cid=450>moment of inertia</portal> and rotating objects. We could endless talk how mind blowing this part of physics is. In stead, it is better if you watch the video above where **Walter Lewin** (one of the best Physics educators) explains and demonstrates everything about this weir phenomenon.

## Right hand rule in physics: why is it so useful?

One of the scariest parts of physics is making sense of all the mathematical work one has to do in order to calculate stuff. As we include vectors and several dimensions, this can quickly become an uncontrollable mess that seems to not have anything to do with reality. To solve this problems, physicist have developed some easy tricks to help you navigate these muddy waters.


NEW
==========================================================================================
==========================================================================================
OLD
This vector cross product calculator allows you to calculate a cross product of two arbitrary vectors in a 3D space. Instead of performing tedious manual calculations, you can input the components of two vectors into this calculator and obtain the result in a blink of an eye. Don't worry if you're not an expert on the subject; this article with explain in detail how to calculate the cross product. It will also provide you with the step-by-step derivation of the cross product formula.

## Cross vs. dot product

In general, there are two types of vector multiplication: the cross product (also called the directed area product) and the <portal cid="560">dot product</portal>. The main feature distinguishing them is that the result of a dot operation is a scalar (a single number), and the result of a cross operation is a vector.

## Cross product definition

The cross product of two arbitrary non-collinear vectors **a** and **b** is a vector **c** that is perpendicular to both of them. If you create a plane that both vectors **a** and **b** lie on, then the resultant vector **c** will be normal to that plane. 

The direction of the resultant vector can be determined using the right-hand rule. If the index and middle fingers of your right hand point along the directions of **a** and **b** respectively, then your thumb will indicate the direction of the **c** vector.

For **a** and **b** being collinear, **c** is a zero vector (with all components equal to 0).

## Vector cross product formula 

The main formula used for calculating the vector cross product is derived from its definition. The equation is as follows:

`c = a × b = |a| * |b| * sinθ * n`,

where:

* **a** and **b** are arbitrary vectors,
* |**a**| and |**b**| are the magnitudes of these vectors,
* **c** is the resulting vector cross product,
* θ is the angle between these vectors, and
* **n** is a <portal cid="553">unit vector</portal> perpendicular to the plane determined by the **a** and **b** vectors. Its direction is established using the right-hand rule. 

For manual computations, we recommend to use the following formula:  

`a × b = (a₂b₃ - a₃b₂) * i + (a₃b₁ - a₁b₃) * j + (a₁b₂ - a₂b₁) * k`

## How to calculate the cross product?

Where did the aforementioned equation come from? We will derive it now so you can get a better understanding of the cross product formula. 

If you want to calculate the cross product manually, you need to know some basic rules resulting from its definition. Consider standard basis vectors **i** = [1, 0, 0], **j** = [0, 1, 0] and **k** = [0, 0, 1]. Then by definition of the cross product,

`i × j = k`

`j × k = i`

` k × i = j`

Similarly, 

`j × i = -k`

`k × j = -i`

` i × k = -j`

As we know that the cross product of collinear vectors is a zero vector,

`i × i = j × j = k × k = 0`

Now that we know these basic rules, it's time to calculate the cross product of two arbitrary vectors: **a** = [a₁, a₂, a₃] and **b** = [b₁, b₂, b₃]. 

First, you need to convert each of the vectors to their equivalent in standard basis vectors:

`a = a₁ * i + a₂ * j + a₃ * k`

`b = b₁ * i + b₂ * j + b₃ * k`

Then, multiply the vectors by each other. It is done simply by multiplying each term of the **a** vector by each term of the **b** vector.

`a × b = (a₁ * i + a₂ * j + a₃ * k) × (b₁ * i + b₂ * j + b₃ * k)`

`a × b = (a₁b₁ * i×i) + (a₁b₂ * i×j) + (a₁b₃ * i×k) + (a₂b₁ * j×i) + (a₂b₂ * j×j) +(a₂b₃ * j×k) + (a₃b₁ * k×i) + (a₃b₂ * k×j) + (a₃b₃ * k×k)`

Each of the cross products between the standard basis vectors can be substituted by its equivalent. We obtain the following formula:

`a × b = (a₂b₃ - a₃b₂) * i + (a₃b₁ - a₁b₃) * j + (a₁b₂ - a₂b₁) * k`
