library(dplyr)
# select() - select columns
# filter() - filter data based on condition
# mutate() - add new variables and transform variable s
# rename() - rename columns
# arrange() - arrange data in asc/desc
# summarise() - usually used with grou_by() to summarise data
# %>% - linking the functions

library(wooldridge)
data(wage1)
wage1 %>% head()

# SELECT()
wage1 %>% select(!c(wage, educ, exper, tenure, female, married)) %>% head()
wage1 %>% select(!lwage:tenursq) %>% head()
wage1 %>% select(c(female, married))%>% head()
wage1 %>% select(everything())
wage1 %>% select(last_col())
wage1 %>% select(starts_with("sq"))
wage1 %>% select(contains("sq"))

# FILTER
wage1 %>% select(wage, tenure, female) %>%
  filter(female == 1) %>%
  head()

wage1 %>% filter(female == 1)

x <- wage1 %>% filter(female == 1 & married == 1)
y <- wage1 %>% filter(female == 1 , married == 1)
identical(x,y)

wage_female_married <- wage1 %>% select(wage,exper ,female, married, numdep, smsa) %>%
  filter(female == 1 & married == 1)
wage_female_married

ggplot(data = wage_female_married, aes(x=wage, y=exper)) + geom_point()


# MUTATING
wage1 %>% mutate(depreciation = numdep ^ 2)

wage1 %>% transmute(dep = numdep ^ 2, 
                    experience = exper / 2) %>%
  head()