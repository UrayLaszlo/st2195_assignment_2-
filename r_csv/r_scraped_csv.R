install.packages("rvest")

library(rvest)

setwd("~/Desktop/Programming/ST2195/Assignment 2/r_csv")

url <- read_html("https://en.wikipedia.org/wiki/Comma-separated_values")

example_csv <- html_nodes(url, "pre")

relevant_line <- read.csv(example_csv)

write.csv(relevant_line[11], file = "cars.csv")

