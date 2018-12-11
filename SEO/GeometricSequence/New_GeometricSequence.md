## Geometric sequence equation and geometric sequence definition

As found on the (https://en.wikipedia.org/wiki/Geometric_progression)[Wikipedia] the geometric sequence definition is: _a collections of numbers in which all by the first one are obtained by multiplying the previous one by a fixed, non-zero number called the common ratio_. If you are struggling to understand what is a geometric sequences just by reading this, **don't fret!** We will explain in more simple terms what this means and take a look at the recursive and explicit formula for a geometric sequence, and we will **also include a couple of geometric sequence examples**.

Before we dissect the definition properly it's important to clarify a **few things to avoid confusion**. First of all we need to understand that even though the geometric progression is made up by constantly multiplying numbers by a factor, this is not related to the <portal cid=395>factorial</portal>. What it is indeed related is to the greatest common factor (GFC) and Lowest Common Multiplier (LCM)</portal> since all but the first number share a common factor. 

This means that the <portal cid=169>GCF</portal> is simply the _commmon ratio_ to a different power (the <portal cid=158>exponent</portal> depends on what terms from the sequence we are considering). Conversely, the <portal cid=169>LCM</portal> is just the smallest of the number we are interested in.

## Geometric progression: What is a geometric sequence/progression?

Let's see now what is a geometric sequence in _layperson_ terms. A geometric sequences is a collection of specific numbers that are related by the common ratio we have mentioned before. The <portal cid=258>ratio</portal> is one of the defining features of a given sequences and together with the initial term of the sequence. We will see later how this two numbers are at the basis of the geometric sequence definition and depending on how they are used one can obtain the explicit formula for a geometric sequence or the equivalent recursive formula for the geometric sequence.

Now we will construct a simple geometric sequence using concrete values of this two defining parameters. To make things simple we will take the initial term to be `1` and the ratio will be set to `2`. In this case we have the first term been `a₁ = 1` by definition; the second term would be `a₂ = a₁ * 2 = 2`, the third term would then be `a₃	= a₂ * 2 = 4`... Etc. The _n-th_ term of the progression would then be 
`aₙ = 1 * 2ⁿ⁻¹`
Where `n` would be the position of said term in the sequence.

A common way to write a geometric progression is to **explicitly write down the first terms**. This allows you to calculate any other number in the sequence; for our example we would write the series as:
`1, 2, 4, 8...`
However there are more mathematical ways to provide the same information. These other ways are the so-called explicit and recursive formula a for geometric sequence. Now that we understand perfectly what is a geometric sequence we can dive deeper into this formulas and explore the mathematical way of conveying the same meaning in less words and with more precision.

## Explicit formula of a geometric sequence vs recursive formula of a geometric sequence

There exists two distinct ways in which you can **mathematically represent a geometric sequence with just one formula**: the explicit formula for geometric sequence and the recursive formula for geometric sequence. The first one of the two is the one we have already seen in our geometric series example. What we saw was the specific explicit formula for our geometric series example but you can write a formula that is valid for any geometric progression. From this general formula one can substitute the values of `aₙ` for the corresponding initial term and `r` for the ratio. The general formula for the n-th term is: 
`aₙ = a₁ * rⁿ⁻¹  n ∈ 𝗡 `
The recursive formula for geometric sequence conveys the most important information about a geometric progression: the initial term `a₁`, how to obtain any term from the first one, and the fact that there is no term before the initial (`n ∈ 𝗡 ` means that `n =1, 2, 3, ...`)

There is another way to show the same information, another type of formula: the recursive formula for geometric sequence. This formula is made of two parts that convey different parts of the geometric sequence definition. The first part explains how to get from any member of the sequence to any other member using the ratio. This meaning alone is not enough to construct a geometric sequence from scratch since we do not know the starting point. This is the **second part of the formula, the initial term** (or any other term for that matter). Let's see how this recursive formula looks:
`aₙ = aₙ₋₁ * r`
`aᵢ = x`
Where here `x` is used to express the fact that any number will be used in its place, but that it must be a explicit number and not a formula. The subscript `i` indicates any natural number (just like `n`) but it's used instead of `n` to make it clear that `i` does not need to be the same number as `n`.

## How to use the Geometric sequence calculator

Now that you know what is a geometric sequence and how to write both the recursive and explicit formula for a geometric sequence is time to **apply our knowledge and calculate some stuff**! With our geometric sequence calculator you can calculate the most important values of a finite geometric sequence. These values include **the common ration, the inital term, the last term and the number of terms**. Let's see a brief description of them in the following list:

* `Initial term`: First term of the sequence
* `Common ration`: Ratio between the term aₙ and the term aₙ₋₁
* `Number of terms`: How many numbers does out geometric sequence contain
* `N-th term`: Value of the last term
* `Sum of the first N terms`: Result of adding up all the terms in the finite series
* `Infinite sum`: Sum of all terms possible from `n=1` to `n=∞`

This terms are all known to us already, except the last 2, about which we will talk in the following sections. If we ignore the summation components of the geometric sequence calculator, we will need to introduce 3 of the 4 values to obtain the 4th element. The sums are automatically calculated from this values; but seriously, don't worry about it too much, we will explain what they mean and how to use them in the next sections.

## Geometric series formula: sum of a geometric sequence

So far we have talked about geometric sequences or geometric progressions, which are collections of numbers. However there are really interesting results to be obtained when we try to sum the terms on a geometric sequence. When we have a finite geometric progression, which has a limited number of terms, the process here is as simple as finding the <portal cid=308>sum of a linear number sequence</portal>. Calculating the sum of this geometric sequence can even be done by hand, in principle.

We can be more efficient than that by using the geometric series formula and plating around with it. To do this we will use the mathematical sign of summation (`∑`) which means summing up every term after it. For example if we have a geometric progression named `P` and we name the sum of the geometric sequence (its associated geometric series) `S`, the relationship between both would be: 
`S = ∑ P`
This is the first geometric series formula we see and the simplest, but it is also not how a mathematician would write it. In mathematics geometric series and geometric sequences are typically denoted just by their general term `aₙ`, so the geometric series formula would look like this:
`S = ∑ aₙ = a₁ + a₂ + a₃ + ... + aₘ` 
Where `m` is the total number of terms we want to sum. 
Unfortunately this still leaves you with the problem of actually calculating the value of the geometric series. You could always use this calculator as a geometric series calculator (we will show you how later) but it would be much better if before using any geometric sum calculator you could understand how to do it manually. There is a that can make our job much easier and involves tweaking and solving the geometric sequence equation like this: 
`S = ∑ aₙ = ∑ a₁ * rⁿ⁻¹ = a₁ + a₁ * r + a₁ * r² + ... + a₁ * rᵐ⁻¹`
Now multiply both sides by `(1-r)` and solve:
`S * (1-r) = (1-r) * (a₁ + a₁ * r + a₁ * r² + ... + a₁ * rᵐ⁻¹)`
`S * (1-r) = a₁ + a₁ * r + a₁ * r² + ... + a₁ * rᵐ⁻¹ - a₁ * r - a₁ * r² - ... - a₁ * rᵐ = a₁ - a₁ * rᵐ` 
`S = ∑ aₙ = a₁ - a₁ * rᵐ / (1-r)`
Which is a result you can easily compute compute on your own and represents the basic geometric series formula, when the number of terms in the series in finite. However, this is maths and not the Real Life™ so we can actually have an infinite number of terms in our geometric series and still be able to calculate the total sum of all the terms. How does this wizardry work? - I hear you ask-. Well fear not for **we shall explain all the details to you, found apprentice**.

## From the geometric sequence formula to a geometric sum calculator for infinite terms

After seeing how to obtain the geometric series formula for a finite number of terms, it is natural (at least for mathematicians) to ask _how can I obtain the infinite sum of a geometric sequences?_ It might seem impossible to do so but there are certain tricks that allow us to calculate this value in simple steps. For this we need to introduce the concept of _limit_. This is a mathematical process by which we can understand what happens at infinity or in cases where we find a mathematically undefined expression such as `0/0` or `0⁰`. 

Talking about limits is a very complex subject and it goes beyond the scope of this calculator. It is for this reason that we have decided to just mention them and not actually go in detail as to how to calculate them. Do not worry, thought, because you can still calculate the infinite sum of a geometrical series using our calculator. The only thing you need to know is that not all series have a defined sum; the conditions that a series has to fulfil for its sum to be a number (this is what mathematicians call _convergence_) are simple in principle, so we will explain them in the following section.

## Remarks on using the calculator as a geometric series calculator

When it comes to mathematical series (from both geometric and <portal cid=509>arithmetic sequences</portal>) they are often grouped in two different categories depending on whether their infinite sum is finite (convergent series) or infinite or non-defined (divergent series). The best way to know if a series is convergent or not is to calculate their infinite sum using limits, but short of that there are some tricks that can allow us to rapidly distinguish between convergent and divergent series without having to do all the calculations. This tricks include: looking at the initial and general term, looking at the ratio, comparing with other series.

For a series to be convergent the general term (aₙ) has to always get smaller as we increase the value of `n`. If `aₙ` gets smaller we cannot guarantee that the series will be convergent but if `aₙ` is constant of gets bigger as we increase `n` we can definitely say that the series will be divergent. If we are not sure whether `aₙ` gets smaller or not, we can simply look at the inital term and the ratio, or even calculate some of the first terms. This will give us a sense for how `aₙ` evolves.

The second option we have is to compare the evolution of our geometric progression against one that we know for sure converges (or diverges), which can be done with a quick search online. Speaking broadly if the series we want to know about is smaller than one that we know for sure that converges, we can be certain that our series will also converge. Conversely if our series is bigger than one we know for sure is divergent, our series will always diverge. In the rest of the cases (bigger than a convergent or smaller than a divergent) we cannot say anything about our geometric series and we are forced to find another series to compare to or to use another method.

These criteria apply for arithmetic and geometric progressions. In fact these two are closely related with each other and both sequences can be linked by the operations of exponentiation and taking <portal cid=470>logarithms</portal>

## Zeno's paradox and other geometric sequence examples

We have already seen a geometric sequence example in the form of the so-called _Sequence of powers of two_. This is a very important sequence because of computers and their usage of binary representation of data. In this progression we can find values such as the maximum allowed number in a computer (varies depending on the type of variable we use), the numbers of <portal cid=220>bytes</portal> in a gigabyte, or the number of second till the end of <portal cid=1118>UNIX time</portal> (both original and _patched_ values).

On top of the power-of-two sequence, we can have any other power sequence if we simply replace `r = 2` with the value of the base we are interested in. Power series are commonly used and widely known and can be expressed using the convenient geometric sequence formula. But this power sequences of any kind are not the only sequences we can have, and we will show you even more important or interesting geometric progressions like the alternating series of the mind blowing Zeno's paradox.

Let's start with Zeno's paradox, a paradox that at its core is just a mathematical puzzle in the form of an infinite geometric series. Zeno was a Greek philosopher the pre-dated Socrated. He devised a mechanism by which he could prove that movement was impossible and should never happen in real life. The idea is to divide the distance between the starting point (A) and the finishing point (B) in half. Once you have covered the first half you divide the remaining distance half again... You can repeat this process as many times as you want which means that you will always have some <portal cid=144>distance</portal> left to get to point B.

Zeno's paradox seems to predict that, since we have an infinite amount of halves to walk, we would need an infinite amount of time to travel from A to B. However, as we know from our everyday experience this is not true and we can always get to point A to point B in a finite amount of time (except for Spanish people that always seem to arrive infitely late everywhere). The solution to this apparent paradox can be found using maths.

If we express the time it takes to get from A to B (let's call it `t` for now) in the form of a geometric series we would have a series defined by: `a₁ = t/2` with the common ratio being: `r = 2`. So the first half would take `t/2` to be walked, then we would cover half of the remaining distance in `t/4`, then `t/8`, Etc.. If we now perform the infinite sum of the geometric series we would find that:
`S = ∑ aₙ = t/2 + t/4 + ... = t*(1/2 + 1/4 + 1/8 +...) = t * 1 = t`
Which is the mathematical proof that we can get from A to B in a finite amount of time (`t` in this case). 

To finish it off, and it case Zeno's paradox was not enough of a mind-blowing experience, let's mention the alternating unit series. This series starts at `a₁ = 1` and has a ratio `r = -1` which yields a series of the form: 
`S = ∑ aₙ = 1 - 1 + 1 - 1 + ...`
Which seems to not converge since the result depends on where we take an even (`S = 0`) or odd (`S = 1`) number of terms. There is a trick by which, however, we can make this series converge to one finite number. The trick itself is very simple but it is cemented on very complex mathematical (and even meta-mathematical) arguments so if you ever show this to a mathematician you risk getting into big trouble, you've been warned. Let's see the _"solution"_:
`S = 1 - 1 + 1 - 1 + ...`
We multiply both sides by `-1`:
`-S = -1 + 1 - 1 + 1 - ... = -1 + (1 - 1 + 1 - 1 + ...) = -1 + S`
If we solve for `S` now:
`-S - S = -1 →  2S = 1 →  S = 1/2`

Now you can go and show-off to your friends, as long as they are not mathematicians.




NEW
=======================================================================================
