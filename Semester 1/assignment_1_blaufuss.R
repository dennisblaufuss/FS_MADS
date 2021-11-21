# Assignment 1
# Dennis Blaufuss

# Task 1
p_grid_1 <- seq(from = 0 , to = 1, length.out = 1000)
prior_1 <- rep(1, 1000)
likelihood_1 <- dbinom(6, size = 9, prob = p_grid_1)
posterior_1 <- likelihood_1 * prior_1
posterior_1 <- posterior_1 / sum(posterior_1)
set.seed (215)
samples <- sample(p_grid_1, prob = posterior_1, size = 1e4, replace = TRUE)

plot(p_grid_1, posterior_1, type="l",
     xlab = "probability", ylab = "posterior")
mtext( "Task 1")

# A)
p_below_twenty <- sum(posterior_1[p_grid_1 < 0.2])
p_below_twenty_sampled <- sum(samples < 0.2) / 1e4

# B)
p_above_eighty <- sum(posterior_1[p_grid_1 > 0.8])
p_above_eighty_sampled <- sum(samples > 0.8) / 1e4

# C)
p_between <- sum(posterior_1[p_grid_1 < 0.8]) - 
             sum(posterior_1[p_grid_1 <= 0.2])
p_between_sampled <- sum(samples >= 0.2 & samples < 0.8) / 1e4

#' I interpreted the word "between" as 0.2 < X < 0.8
#' Hence we have to use <= 0.2 in line 27 & 28. To be exact in this case it is 
#' not relevant since there is no p_grid_1 for exactly 0.2. Still I think this
#' is important to be stated.

# D)
sum  <- 0
i <- 1
while (sum < 0.2)
{
  sum = sum + posterior_1[i]
  i <- i + 1
}
i <- i - 1
quantile_twenty <- p_grid_1[i]
quantile_twenty_sampled <- quantile(samples, 0.2)

#' To be exact under a probability of i_twenty there lies a bit more than 20% 
#' of the posterior probability. IMO this is definition wise the correct answer.
#' But one may argue that we have to choose p_grid_1[i - 1].

#' General disclaimer regarding task 1:
#' I recon in all of this cases the non sampled variant may be the one to be
#' chosen since it is available in this scenario and more precise. Furthermore,
#' thinking large scope it would cost less since we don't need to create the 
#' sample in the first place.

# Task 2
# A)
p_grid_2 <- seq(from = 0 , to = 1, length.out = 1000)
prior_2a <- rep(1, 1000)
likelihood_2 <- dbinom(8, size = 15, prob = p_grid_2)
posterior_2a <- likelihood_2 * prior_2a
posterior_2a <- posterior_2a / sum(posterior_2a)

plot(p_grid_2, posterior_2a, type="l",
     xlab = "probability", ylab = "posterior")
mtext( "Task 2A")

# B)
prior_2b <- prior_2a
prior_2b[p_grid_2 < 0.5] <- 0
posterior_2b <- likelihood_2 * prior_2b
posterior_2b <- posterior_2b / sum(posterior_2b)

plot(p_grid_2, posterior_2b, type="l", col="red",
     xlab = "probability", ylab = "posterior")
mtext( "Task 2B")

#' What is the difference between these two models?
#' See graphics: In the second case every posterior probability for a 
#' probability up to 0.5 is zero (key word multiplication)

#' How does each posterior distribution compare to the true value of p=0.7?
#' The second one does better but still not optimal. While the mean of it is 
#' closer to 0.7 (in comparison to option 1) the mode is still not placed in a
#' optimal position. To get a better result we would need to recompute priors 
#' and do it over again. AKA task 3 :D

#' Which prior is better and why?
#' Second one (under assumption of given true value of question before):
#' We know for a certain that p won't be below 0.5 so with setting those priors
#' to 0 we aggregate more probability in the relevant area.
#' At first sight if we have both graphs in different coordinate systems the 
#' difference seems minor. But putting them into the same one shows mentioned 
#' aggregation around the relevant area.

plot(p_grid_2, posterior_2b, type="l", col="red",
     xlab = "probability", ylab = "posterior")
lines(p_grid_2, posterior_2a, type="l")
mtext( "Comparison")

# Task 3

#' IMO the Task is interpretable in two ways: 
#' 1. The p that in interval is around is the known-to-be-true 0.7
#' The solution to this interpretation is simply to get the quantile for 
#' 0.675 < X < 0.725 and repeat until this reached 0.99. Again, the sample as
#' well as the grid can be used.
#' 2. The p that in interval is around is the mean of according posterior 
#' distribution
#' Since I was not yet able to get my toolchain and thus rethinking working
#' i was not able to use the "PI" function within that package. I used the "CI"
#' function from the Rmisc lib. Since with bettering the prior we get closer
#' closer to a normal distributed and thus symmetrical function the difference
#' should not be notable.

library(rethinking)

simulations <- 100
throws <- c()
means <- c()
while (length(throws) <= simulations){
  p_grid_3 <- seq(from = 0 , to = 1, length.out = 1000)
  prior_3 <- rep(1, 1000)
  posterior_3 <- prior_3
  water_counter <- 0
  land_counter <- 0
  throw_counter <- 0
  width <- 1
  percent_in_p_range <- 0
  
#  while (percent_in_p_range < 0.99){
 while (width >= 0.05){
    throw_counter <- throw_counter + 1
    if (runif(1) < 0.7) 
      water_counter <- water_counter + 1
    else 
      land_counter <- land_counter + 1
    prior_3 <- posterior_3
    likelihood_3 <- dbinom(water_counter, size = throw_counter, prob = p_grid_3)
    posterior_3 <- likelihood_3 * prior_3
    posterior_3 <- posterior_3 / sum(posterior_3)
    samples_3 <- sample(p_grid_3, prob = posterior_3, size = 1e4, replace = TRUE)
    percent_in_p_range <- sum(posterior_3[p_grid_3 < 0.725]) 
                          - sum(posterior_3[p_grid_3 < 0.675])
    width <- PI(samples_3, 0.99)[2] - PI(samples_3, 0.99)[1]
    names(width) <- NULL
  }
  throws <- c(throws, throw_counter)
  means <- c(means, mean(samples_3))
}

#' As to be expected for the first option way more throws are required. But
#' it hits the 0.7 obviously more effective. Count of throws are ranging
#' between a large span each simulation. A rough estimate is that the mean is
#' around 180. 
#' The second option is relatively stable at a mean of 65 throws. But therefore
#' it is not as exact with hitting the 0.7. It averages out pretty good but
#' there are even some cases at 0.5 and up to 0.99.
#' From a practical view I actually think option two has more relevancy since
#' in practice you almost never now the true p (as in this example p = 0.7)
#' Thus if I'd had to give a final answer I would say:
#' We would have to throw the globe approximately 65 times to receive a p for
#' percentage of Water on Earth with p being within a 99% interval with a width
#' of max 0.05.
