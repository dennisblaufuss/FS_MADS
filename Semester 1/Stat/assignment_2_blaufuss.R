# Assignment 2
# Dennis Blaufuss

library(rethinking)
library(dagitty)

1. Consider the following model from the textbook to use the !Kung census to predict height from weight of adults.

data(Howell1)
d <- Howell1
d2 <- d[d$age >= 18, ]
xbar  <- mean(d2$weight)
m4.3 <- quap(
  alist(
    height ~ dnorm(mu, sigma),
    mu <- a + b * (weight - xbar),
    a ~ dnorm(178, 20),
    b ~ dlnorm(0, 1),
    sigma ~ dunif(0, 50)
    ),
  data = d2
)

Using this model, provide the predicted heights and 89% credibility intervals for each of the following individuals:

weight.seq <- c(46, 61, 35, 52, 56)
sim.height <- sim(m4.3, data = list(weight = weight.seq), n=1e4)
height.hat <- apply(sim.height, 2, mean)
height.PI <- apply(sim.height, 2, PI, prob = 0.89)
data.frame(
  individual = 1:5,
  weight = weight.seq,
  expected_heigth = height.hat,
  '5%' = height.PI[1, ],
  '95%' = height.PI[2, ]
)

One may argue that using "median" would be the way to go. But since 
we give the information of an interval as well i wanted to use mean in order
to secure that the interval will be spanned around my expected height.

 
2. Plot the prior predictive distribution for the polynomial regression model in Chapter 4. Use extract.prior to inspect the prior, and modify the code that simulates and plots prior predictive distributions for linear regression to perform prior predic- tive simulations. Plotting between 30 and 50 parabolas from the prior should suffice to show where the prior probability resides. Can you modify the prior distributions of α,β1 and β2 so that the prior predictions stay within the biologically reasonable out- comes? You should not attempt to fit the data by hand. Instead, try to keep the curves consistent with what you know about height and weight before seeing the !Kung data.

data(Howell1)
d <- Howell1
d$weight_s <- (d$weight - mean(d$weight)) / sd(d$weight)
d$weight_s2 <- d$weight_sˆ2
m4.5 <- quap(
  alist(
    height ~ dnorm(mu, sigma),
    mu <- a + b1 * weight_s + b2 * weight_s2,
    a ~ dnorm(178, 20),
    b1 ~ dlnorm(0, 1),
    b2 ~ dnorm(0, 100),
    sigma ~ dunif(0, 50)
  ),
  data = d
)

prior <- extract.prior(m4.5)

weight.seq <- seq(from = -2.2, to = 2, length.out = 30) 
pred_dat <- list(weight_s = weight.seq, weight_s2 = weight.seqˆ2)
mu <- link(m4.5, post = prior, data=pred_dat)

plot(NULL, xlim = range(weight.seq), ylim = c(-50, 300),
     xlab = "Standard Deviation of Weight", ylab = "Height")
abline(h = 0, lty = 2)
abline(h=272, lty = 1)
for (i in 1:50){lines(weight.seq, mu[i,], col = col.alpha("black", 0.4))} text(-2.6, 280, "World's tallest person (272cm)", adj = c(0, 0)) text(-2.6, -30, "Embryo", adj = c(0, 0))


3. Write down a multiple regression to evaluate the claim: 1
The price of houses in Frankfurt is linearly related to size, but only after controlling for location (i.e., postal code).
You only need to write down the model definition.
There are 41 postal codes in Frankfurt. For this exercise, consider houses to belong to one of four postal code regions: 603**, 604**, 605**, and 659**.

Pi ∼Normal(μi,σ)
μi = α + βsSi + β603Z603i + β604Z604i + β605Z605i + β659Z659i
with S = Size, Z = Zipcode, P = Price and β = weigth

4. In the divorce example, suppose the DAG is: M → A → D. 
dag <- dagitty("dag{ M -> A -> D}")
coordinates(dag) <- list( x=c(A=0,D=1,M=2) , y=c(A=0,D=1,M=0) )
drawdag(dag)

What are the implied conditional independencies of this graph?

impliedConditionalIndependencies(dag)
D _||_ M | A
D and M are conditionally independend under the condition of knowing A.

Are the data consistent with it?




