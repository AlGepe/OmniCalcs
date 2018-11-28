Welcome to the factorial calculator: a tool that **calculates the factorial of any integer from 0 to a 170**. On top of calculating the 0-factorial, 5-factorial... We will also show you how to use the exclamation point in maths, provide **information about the n-factorial formula and the applications** it can have. We will answer the question of "what is a factorial?" using the factorial definition. We will dive into the maths behind it to find how we can include more than just positive integers, using the gamma function.

## Exclamation point in Maths: What is a factorial?

 When you see for the first time an **exclamation point in maths** you probably got shocked or even thought you that there was some kind of mistake or typo. But the reality is different: this exclamation point in maths **is called the factorial** or n-factorial. The factorial is a fairly unknown operator that in reality can be viewed more as an abbreviation than a true operator in itself, at least at the beginning.
 
 <p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_FactWat.jpg"alt="When you see an exclamation point in maths" style="width:70%" align="center"><br><strong><sup><i>When you see an exclamation point in maths </i></sup></strong></p>

It is important not to confuse the factorial with <portal cid=143>prime factorization</portal> which is a way of obtaining the prime numbers that when multiplied give you a known number. Prime factorization has its uses in maths and is arguably more known than the n-factorial. Part of the reason prime factorization is more popular is its usefulness when calculating <portal cid=169>Greatest Common Factor</portal> and the <portal cid=170>Least Common Multiplier</portal>, but we are digressing now.

To understand what the factorial does or means we should start with an example. We could choose any number `n` and calculate its n-factorial value, but the best is to choose a fairly small number, so let's use 5-factorial.

`5! = 5 * 4 * 3 * 2 * 1 = 120`

From this example, you can see that it is not <portal cid=978>rocket</portal> science, and you might even take a guess at the factorial formula. You can also understand why this exclamation point in maths can be regarded as an abbreviation since it is not a new operation but rather a collection of multiplications. In short and somewhat informally we can define the factorial as the multiplications of all the positive integers smaller or equal than the given number. 

Playing a bit with this, we can see that for 5-factorial we can relate it to 4-factorial in a straightforward way:

`5! = 5 * (4 * 3 * 2 * 1) = 5 * 4!`

This kind of relationships between n-factorials with different `n` is the basis of the mathematical formula that defines the factorial operation, as we will see in the next section.

The factorial operation is not used everywhere in maths but it is very important in statistics and probability problems. In those cases, especially when one has to deal with <portal cid=427> permutation calculators </portal> or combinatorics, the n-factorial appears almost all the time. We will see real-world examples of problems that require the usage of factorials and the factorial formula.

## Getting mathematical: Factorial definition and Factorial formula

So far we have seen a rather loose explanation of what is a factorial but we have not given a **proper factorial definition**. Well, that is precisely the aim of this section: to see and explain the factorial formula and how we can infer from it the factorial definition in a more mathematical way. 

For a more mathematical description of the factorial formula let's look at the **n-factorial and how that would relate to other factorials**. In this case, `n` can be any number. If we look at the previous examples with 5-factorial, we can see that 

`5! = 5 * 4! = 5 * (5-1)!`

If we now extrapolate that to the n-factorial:

`n! = n * (n-1)!`

Which is the general factorial formula and is an integral part of the factorial definition. However, this **does not answer all the questions about factorials**. For example, what would happen if we take a negative number? When do I stop subtracting numbers? These are valid questions that the factorial formula we have shown doesn't answer but are fundamental for having a proper factorial definition.

These two questions can be answered easily by stating that the factorial formula is **only defined for positive integers**, which means that we cannot go lower than `n = 1`. But this also brings up another question: What is the 0-factorial? Since we cannot use this formula, you are forgiven for thinking that this question has no answer and the whole factorial thing is "fake news". However, there is a 'trick' to get around this: **setting the value of the zero-factorial to a number** by definition.

And, hence, we arrive at the convention:

`0! = 1`

A small disclaimer is needed here since in maths things are never as easy as "choose a number a roll with it", there are **many complex reasons** as to why the value of zero-factorial has been set to `1` and not any other number. Explaining these reasons in detail is far beyond the scope of this factorial calculator.

## Basic values of factorials

Let's check now some of the value for the n-factorial of several small `n`, like zero factorial (0 factorial), 5 factorial, 3 factorial... Pay special attention to the value of 0 factorial because it is **the most important one and we will talk more about it later**.

* 0! = 1
* 1! = 1
* 2! = 2
* 3! = 6
* 4! = 24
* 5! = 120
* 6! = 720
* 7! = 5040
* 8! = 40 320
* 9! = 362 880
* 10! = 3 628 800

We can see how fast the factorial of a number increases as we keep using bigger numbers. This is yet another situation where  <portal cid=161>scientific notation</portal> can save the day (if we know how to properly truncate to the necessary <portal cid=392>significant figures</portal>) if you need to work with such big numbers. For factorials of numbers greater than 10, don't hesitate to **use the factorial calculator above**.

## 0-Factorial and why it is so special

The 0-factorial is a key part of the factorial definition. To understand why it is so important we can show the problems when we try to calculate the zero-factorial using the factorial formula above:

`0! = 0 * (0-1)!` 

It looks like no matter what the value of `(0-1)!` turns out to be, the result should always be `0! = 0` but things are more complicated than that in maths. We saw in the previous section that the n-factorial is only defined for n > 0, so we have a problem here.`(0-1)!` is what mathematicians call: **undefined expression** which means that the expression is not correct and thus it has no mathematical meaning. This is the same problems as with division by zero, it's not that we cannot calculate it, the problem is that **the expression doesn't make sense**, it doesn't have a meaning.

This is a reason why `0!` is important to define as a convention value. Setting it's value to `0! = 0` would not be a good idea since it would mean that `n! = 0` for any value of `n`. You can see why by **applying the factorial formula**. On the other hand, if we set zero-factorial to `1` we now **retain the expected values for n-factorial** while having a simple convention for the value of `0!`. 

We will see in the following section another reasoning behind setting zero-factorial to be equal to `1`, with a more mathematical logic. In doing that we will also introduce the **Gamma function** which is in plain terms an **extended factorial formula** that includes all positive numbers and the 0-factorial.

## Gamma function: Factorials of non-integer values

It is possible to **determine the factorial of non-integer numbers** - basically, for all real numbers excluding negative integers. It requires the use of sophisticated mathematical tools so we will try to give a simpler version here, retaining as much accuracy as we can. In fact, there have been several approaches to extending the **factorial formula to include all positive numbers**, each of them with subtle differences and all of them mostly compatible with each other.

 <p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_FactGraph.png" alt="Gamma function plotted" style="width:70%" align="center"> </p>

Let's start with the Gamma function. The **Gamma function is a function that extends the notion of the n-factorial beyond integers**. Obviously, the formula cannot be the same as we have used before because we would end up on a dead-end. In fact, this function extends the n-factorial to **complex numbers as well**, where the intuitive notion of a factorial is much harder to grasp.

    `𝚪(z) = ∫tᶻ⁻¹ e⁻ᵗ dt`

That's the definitions of the Gamma function, where `t` is the variable of integration and `z` is a **complex number with a positive real part**. This formula reduced to the n-factorial when applied over any positive integer `n`. 

    `n! = 𝚪(n+1)`
    
You can see 2 things from this formula: (1) The Gamma function is much more complicated to use than the n-factorial formula for integers and (2) it is not an exact copy of the n-factorial since you need to calculate the value of the Gamma function for `n+1` to obtain `n!`. To remedy the second "_problem_" we can **introduce the Pi function**.

    `𝚷(z)= ∫tᶻ e⁻ᵗ`

The Pi function is very similar to the Gamma function but shifted just enough so that **the factorial and the function would match up**.

    `𝚷(n) = n! n ∈ 𝗡` 

After all, you might be bewildered by the complexity of the maths behind this factorial formula, but **don't fret!**. As a simple trick, we can tell you that `(-0.5)! = √π` and `(0.5)! = 0.5√π`.

Interestingly, the first factorial formula is still valid here. So, for example,

`(2.5)! = 2.5 * (1.5)! = 2.5 * 1.5 * (0.5)! = 1.875√π`

## Real-world applications

We have already discussed that the factorial is commonly used in probabilistic calculations, permutations... But there is more to it, so let's see what **other places** does the n-factorial appear. Keeping within the realm of pure maths, we arrive at the <portal cid=430>binomial distribution</portal> that helps calculate probabilities of, for example, independent experiments having similar results.

 <p style="text-align:center;"><img src="https://uploads-cdn.omnicalculator.com/images/Al_FactStatPhysics.png" alt="Entropy increase in statistical physics" style="width:70%" align="center"> </p>


Aside from pure maths, the n-factorial appears in many other calculations, most notably in **statistical physics and particle physics** which are parts of physics that deal with permutations of particles, amongst other things. In particular statistical physics is a very useful area of physics that can be thought of as a "_microscopic_" version of thermodynamics. That is because statistical physics deals with thermodynamics problems (like calculating the <portal cid=1060>latent heat</portal> or the <portal cid=442>thermal conductivity</portal>) but it **does it from from a particle-by-particle basis**.

There are other areas (mostly of physics) that use factorials for calculation and we could dive very deep into how and why they use the factorial formula in their calculations, but for a simple calculator like this one that would be well beyond its reach.

## Python factorial and how to calculate factorial in programming languages

In our modern world the **tedious calculations are generally left off to the computers** (just like you're doing by using this calculator). Increasingly common is the usage of coding languages to **create small programs** that will make those calculations for us. The n-factorial is a perfect candidate since it's not really complex conceptually. But for big numbers, it requires too much time for humans to calculate. For those of you that are using programming languages, we will leave you some example for some of the most coding languages.

* **Python factorial**(after 2.6): Use `math.factorial(x)` to get the Python factorial values
* **Java factorial**: There is no 'Java factorial' method in the standard Java packages.
* **Factorial matlab**: To calculate a factorial matlab uses `factorial(x)`. More information on the factorial matlab function can be found on the <a href="https://www.mathworks.com/help/matlab/ref/factorial.html">official documentation</a>
* **Factorial in excel**: Use `FACT` to calculate the factorial in excel. [The factorial in excel only works with integers]
* **Factorial c++**: There is no factorial c++ function included in the standard libraries. See here an example of a <a href="https://www.programiz.com/cpp-programming/examples/factorial">factorial c++ function</a>
* **Factorial javascript**: There is not factorial javascript function included in the standard libraries

