applicants <- read.csv("mapdata.csv")


min(na.omit(as.numeric(as.character(applicants$Population.Based.on.2016.Census))))

applicants[applicants$Population.Based.on.2016.Census %in% "185",]

data.class(applicants)

dim(applicants)

colnames(applicants)

Name.of.community <- as.character(applicants$ï..Name.of.community)
Finalist <- applicants$Finalist
levels(Finalist)[1] <- 0
levels(Finalist)[2] <- 1
Province <- applicants$Province.or.Territory

Population <- applicants$Population.Based.on.2016.Census
Population <- as.numeric(gsub(pattern = ",",replacement = "",as.character(Population)))

Funding <- applicants$Prize.category
Focus.area <- applicants$Focus.areas


library(ggplot2)

Name.of.comminity <- as.character(applicants$ï..Name.of.community)
Finalist <- applicants$Finalist
levels(Finalist)[1] <- 0
levels(Finalist)[2] <- 1
Finalist <- as.numeric(as.character(Finalist))
Province <- applicants$Province.or.Territory

Population <- applicants$Population.Based.on.2016.Census
Population <- as.numeric(gsub(pattern = ",",replacement = "",as.character(Population)))
demodata1 <- (cbind(Finalist, Province, Population))

# write.csv(demodata1, "demodata1.csv")

# first simple dot plot
plot(Population,Finalist)
logpop <- log(Population)
demodata2 <- as.data.frame(c(data.frame(Population),
                             data.frame(logpop),data.frame(Finalist)))

# point yes/no vs population
ggplot(data = demodata2,aes(Finalist,Population))+geom_point()

# boxplot yes/no vs log(population)
ggplot(data = demodata2,aes(Finalist,logpop))+geom_boxplot()

# Funding -> 5/10/50 in million
Funding <- applicants$Prize.category
levels(Funding)[1] <- 10
levels(Funding)[2] <- 5
levels(Funding)[3] <- 50
Funding <- as.numeric(as.character(Funding))
    
    # fund <- glm(Finalist~I(Funding),family = binomial)
    # summary(only.funding)
    # fund.pop <- glm(Finalist~Funding+Population,family = binomial)
    # summary(fund.pop)
    # 
    # fund.logpop <- glm(Finalist~I(Funding)+I(log(Population)),
    #                    family = binomial)
    # summary(fund.logpop)
    # 
    # fund.scaledpop <- glm(Finalist~I(Funding)+I((Population/1000)),
    #                    family = binomial)
    # summary(fund.scaledpop)
    # 
    # AIC(only.funding)
    # AIC(fund.pop)
    # AIC(fund.logpop)
    # AIC(fund.scaledpop)
    # 
    # fund.by.pop <- glm(Finalist~I(Funding*1000000/Population),
    #                    family = binomial)
    # summary(fund.by.pop)

#####################
# scale funding /5 milion and population /10 thousands
fund.scale <- 5
fund <- Funding/fund.scale

pop.scale <- 10000
pop <- Population/pop.scale

scale.fund.pop <- glm(Finalist~fund+pop,family = binomial)
summary(scale.fund.pop)

exp(scale.fund.pop$coefficients)

demodata3 <- cbind(Finalist,fund, pop)
# write.csv(demodata3, "demodata3.csv")

# new merged data
result <- read.csv("result.csv")
attach(result)

fit1 <- glm(good~I(pop/10000)+num.city+
                I(dist.c/100)+I(total.pop/10000)+
                spots + I(dist.s/100)+fund,
            family = binomial)
summary(fit1)

exp(fit1$coefficients)

haha <- c(exp(fit1$coefficients))
# write.csv(haha,'haha.csv')