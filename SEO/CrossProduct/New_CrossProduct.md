Without a vector cross product calculator, this a commonly used algebraic operation, that can get very complicated very quickly. Luckily for you, we've made a tool that helps you understand the cross product formula of two vectors as well as the differences of the dot product vs cross product. In addition, we have also compiled a list of practical uses including the right-hand rule physics trick, so that you can become a wizard in the cross product of two vectors

## Vector cross product definition

A vector is a mathematical tool, **widely used in physics**, that allows you to deal with collections of numbers (dimensions) in a very efficient way. The collection of operations, rules, and properties to deal with vectors is **called vector algebra** and, similarly to the algebra of numbers, it includes multiplication operations. However, operations with vectors are **more complex than with numbers** since they carry much more information that has to be carefully manipulated. This is one of the reasons why in vector algebra there are two different types of multiplications or product operations: the cross product and the <portal cid=560>dot product</portal>.

<p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_CP_vector.png" alt="Picture of a vector" style="width:60%" align="center"> </p>

The definition, as it is common with mathematical stuff, is very technical but we will explain to you what it means in more normal (and less accurate) terms so that even if you don't have a strong mathematical background, **everything will make sense for you**. According to <a href=https://en.wikipedia.org/wiki/Cross_product>Wikipedia</a> the cross product, also called _vector product_ is: 

`Is a binary operation on two vectors in three-dimensional space and is denoted by the symbol ×. Given two linearly independent vectors **a** and **b** the cross product, **a × b**, is a vector that is perpendicular to both **a** and **b** and thus normal to the plane containing them.`

That is indeed a mouthful, but we can translate from mathematical jargon into everyday explanation so that we can all understand it. First of all the definition talks about a **three-dimensional space**, like the one we live in because it is the most common usage of the cross product, but the cross product can be extended to more dimensions; that is, however, **beyond the scope of this text** and most math-related degrees. 

What the definition is telling us is that the **vector cross product of any two vectors is a third vector** that is <portal cid=700>perpendicular</portal> to both of them (and to the plane that contains them). This is possible in 3-dimensional space because in such space there are 3 independent directions. To put it in everyday terms, you can think of these three directions as being **height, width, and depth**.

To know how this new third vector will look like in terms of size, and mathematical description, we will use the **formula for the cross product of two vectors**. In the next section, you will be presented with the formal, mathematical formula that tells you how to do the cross product of any two vectors. As we also do at Omni, we will also **explain what this equation means and how to use it in a simple**, yet accurate way.

## Cross product formula

Before we present to you the formula for the vector product, we need two vectors that we will call `a` and `b`. These **two vectors should not be collinear** (a.k.a. parallel) for reasons that we will explain after we see the formula. We will call the resulting vector from the cross product formula `c`. We also remind you that the letter `n` is used to denote a <portal cid=553>unit vector</portal>(perpendicular to both `a` and `b`. So without further ado let's see the formula:

`c = a × b = |a| * |b| * sinθ * n`,

According to this formula, the resulting vector `c` from performing the cross product between `a` and `b` is a **vector perpendicular to both** (that's where the `n` part of the equation comes in). The modulus/norm/length of this new vector is equal to the "natural" product of the **modulus of each of the initial vectors times the sinus of the angle between them** (`θ`). The fact that there is a factor of perpendicularity, together with the fact that we have a sinus function in the formula are good indicators of the geometrical interpretations of the vector cross product. We will talk more about those when we explain the properties of this mathematical operation.

You can also see in the formula why it is crucial that the two vectors `a` and `b` not be parallel. If they were parallel, that would mean that the angle between both of them will be `θ = 0` and hence we will have both `sinθ = 0` and `c = 0` which is a **very uninteresting result**. This leads, however, into another use for the vector cross product which we will explain later.

## How to do the cross product of two vectors

We have seen the mathematical formula for the vector cross product, but you might still be thinking "_This is all well and good but how do I **actually** calculate the new vector?_" And that is an excellent question. By far the fastest and easiest solution is to use our vector cross product calculator, but if you have read this far, you are **probably looking not only for results but also for knowledge**, so we'll give it to you. We will divide the process into 3 different steps: calculating the modulus of a vector, calculating the angle between two vectors, and calculating the perpendicular unitary vector. Putting all these **three intermediary results together** by means of a simple multiplication will yield the desired vector.

<p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_CP_def.png" alt="Visualisation of the cross product of 2 vectors" style="width:60%" align="center"> </p>

However, **calculating angles between vectors might get too complicated in 3-D space**; and if all we want to do is to compute the cross product between two vectors, it might not be worth the hassle. So let's explore a more straightforward and **practical way of calculating the vector cross product** by means of a different cross product formula. This new formula makes use of the decomposition of a 3D vector into its 3 components. This is a very common way to describe and operate with vectors in which each **component represents a direction in space** and the number accompanying it represents the length of the vector in such direction. Canonically the three dimensions of the 3-D space we're working with are named `x`, `y` and `z` and are represented by the unitary vectors **i**, **j** and **k** respectively.

Following this nomenclature, each vector can be represented by a sum of these three unitary vectors. The vectors are generally omitted for brevity but are still implied and have a big bearing on the result of the cross product. So a vector **v** can be expressed as: `v = (3i + 4j + 1k)` or in short: `v = (3, 4, 1)` where the position of the numbers matters. Using this notation we can now see and understand a straightforward way to calculate the cross product of two vectors, which we will call `v = (v₁, v₂, v₃)` and `w = (w₁, w₂, w₃)`. For these two vectors the formula looks like:

`v x w = ( v₂w₃ - v₂w₃,  v₃w₁ - v₁w₃, v₁w₂ - v₂w₁)`

<later>This result might look like a random collection of operations between components of each vector, but nothing is further from reality. For those of you wondering where this all comes from we encourage you to try and discover it yourself. All you need to do is start with both vectors expressed as: `v = v₁i + v₂j + v₃k` and `w = w₁i + w₂j + w₃k` and multiply each component of a vector with all the components with the other. As a small help or hint, we can tell you that when doing the cross product of vectors multiplied by numbers the result is the "_regular_" product of the numbers times the cross product between vectors, as we will see in the next section. It will also come in handy to remember that the cross product of parallel vectors (and hence of a vector with itself) is always `0` as we've seen before.

For starters let's tackle obtaining the modulus, norm or length of a 3-D vector. For that, we simply need to calculate the <portal cid=291>3d distance</portal> from the beginning to the end of the vector. That can be done using our calculator or by simply taking each of the three components, squaring them, summing them and then performing the <portal cid=151> square root</portal> of the result. Putting it in mathematical terms (using vector `a`) as an example we get:

`|a| = √(a₁² + a₂² + a₃²)`

Where `a₁`, `a₂` and `a₃` represent each of the components of the 3d vector `a`.  </later>

## How to use the vector cross product calculator

So after all the things we've talked about it's time to get to know **how to use our cross product calculator to save time and obtain results** for any to vectors in 3-D space. As you can see, the variables are divided into 3 sections, one for each vector involved in a cross product calculation. Of these three vectors `c` is probably the one you should care about the most since it is the result of the cross product of the other two vectors `a` and `b`. Each vector has 3 components as mentioned before: `x`, `y` and `z` referring to each of the three dimensions (depth, width, and height).  

Once we have understood what each of the fields does, let's take a quick look at a typical use case for this calculator. To include an example for calculating the cross product of two vectors, we will use the vectors: `a = (2, 3, 7)` and `b = (1, 2, 4)`. 

1) The first step is to introduce the components of vector `a`. That is: `x=2`, `y=3` and `z=7`
1) Next, you should introduce the components of vector `b`. That is: `x=1`, `y=2` and `z=4`
1) _Voilà!_ you have just calculated `c = a x b = (-2, -1, 1)`
1) Repeat again until you have calculated all the cross products you needed to
1) Share with your friends the life-changing experience of calculating vector cross products. ;)

You can calculate the cross product of any vectors you want, without even having to think about it. However, we highly recommend you to **use the properties we have mentioned above for complex operations to save you time and hassle**. For example, if one of the vectors is simply a multiple of the other you don't even need to use our calculator, you can just predict that the result will be zero since those to vectors are collinear.

## Dot product vs cross product

We have explored most of the mathematical aspects of the cross product of two vectors in 3-D space, so it's time to talk about some **interesting facts and uses of this vector operation**. To kick things off we will talk about the _cousin_ of the cross product: the dot product. These two operations have a misleadingly close name but in fact, represent different concepts in mathematics and geometry. On top of that computing the dot product is arguably easier than computing the cross product; nevertheless, we have also made a calculator that helps you calculate the <portal cid=560>dot product of 2 vectors</portal>, also **called the scalar product**.

Keeping up with the trend of apparent similarities between the scalar product and the cross product we can take a close look at the formula for the dot product:
`v = a · b = |a|*|b|*cosθ`
where the only differences between the cross product and the dot product are the trigonometric function and the fact that the result is a number (scalar, hence the name) rather than a vector as it was the case with the cross product.

<p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_CP_dot.png" alt="Visualization of the dot product of two vectors" style="width:60%" align="center"> </p>

These small differences might have **you believe that both operations are very similar, but they are very different in nature**. For starters, the cross product is an operation that takes two vectors and returns another vector perpendicular to both, while the dot product yields a number with no direction. The dot product is also much more **easily generalizable to higher or lower dimensions, while the cross product does not even exist in 2-D**. Their interpretation in geometrical terms is also very different since you can think of the dot product as the length of the projection of one of the vectors onto the other.

All those differences make them very distinct operations conceptually and are, therefore, not interchangeable or translatable. Both operations are instrumental in both mathematics and physics as we will see in the following sections.

## Cross product and physics: Best Friends Forever

As always, most of us are not interested just in the purely mathematical properties and uses of the cross product but also in **the practical application in the real world**. And what better way to get a useful application of mathematical concepts than through physics. The cross product is not an exception, and it is a very useful operation in physics. We could get deep into Quantum Field Theory where both the scalar product and the cross product are widely used. However, **we will stay within the realm of tangible and mathematically perfect theories** and look at examples in places and events we can all relate to. 

The first field in which the **cross product properties are widely used is electromagnetism**. In nature, electric and magnetic fields are generally present perpendicular to each other, which ties perfectly into the way the cross product of two vectors is expressed. Thing like calculating the <portal cid=903>magnetic forces on a current-carrying wire</portal> or computations for the <portal cid=970>magnetic moment</portal> of a system, all require the use of the cross product operation. Another example that cannot go unmentioned is the so-called <portal cid=1050>Hall effect</portal> that is a very important effect in solid state physics but whose explanation is far too complicated to be treated here, so **we invite you to visit the calculator we made for such purpose**.

<p style="text-align:center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/NeXIV-wMVUk?start=72" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

An even more accessible place where we can use the cross product formula to predict things is when we talk about <portal cid=450>moment of inertia</portal> and rotating objects. We could have an endless talk about how mind-blowing this part of physics is. Instead, it is better if you watch the video above where **Walter Lewin** (one of the best Physics educators) explains and demonstrates everything about this weird phenomenon.

## Right-hand rule in physics: why is it so useful?

One of the **scariest parts of physics is making sense of all the mathematical work** one has to do in order to calculate stuff. As we include vectors and several dimensions, this can quickly become an uncontrollable mess that seems not to have anything to do with reality. To solve these problems, physicists have developed **some easy tricks to help you navigate these muddy waters**. Probably the most known of these is the "_Right hand rule_" that help in the cross vector product calculation. This rule enables you to predict where the resulting vector of the cross product will be directed by only using your hand and fingers.

<p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_CP_rhr.png" alt="Right hand rule, first version" style="width:60%" align="center"> </p>
There are **two versions of the right-hand rule in physics**: one with the fingers extended and the hand still, and the other involves going from an open hand to a closed fist. The first one is probably the most commonly used and consist of spreading the middle and index finger as shown in the picture. With the thumb also extended you should aim at aligning the index finger with the first vector, and the middle finger with the second one. In this position, the **extended thumb will show the direction of the resulting vector** from computing the vector cross product.

The second method is **in our opinion a easier one to use**. With an open hand, you align the fingers with the first vector. Then you close your hand into a fist towards the second vector. After performing these actions, you will end up with a thumbs-up or thumbs-down hand. As in the previous case, the direction of the thumb will indicate the direction of the vector resulting from the cross product operation.

<p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_CP_Curr.png" alt="Right hand rule, second version" style="width:60%" align="center"> </p>

All this **might seem like childish games**, but they are potent tricks. With a simple hand gesture, you can get an unadulterated perspective on how the vector cross product you want to perform will look like. It might even come as a surprise to you that these tricks **are used continuously by researchers whenever** their work involves any cross product calculations, like when calculating the <portal cid=908>magnetic forces between wires</portal>
