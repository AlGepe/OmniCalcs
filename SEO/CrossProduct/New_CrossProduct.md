## Vector cross product definition
## Cross product properties
## Cross product formula
## How to do the cross product of two vectors
## How to use the vector cross product calculator
## Dot product vs cross product
## Cross product and physics: Best Friends Forever
## Right hand rule in physics: why is it so useful?



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
