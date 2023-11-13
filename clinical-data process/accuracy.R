accuracy <- function(label,prob){
  prob[plogis(prob)>=0.5] <- 1
  prob[plogis(prob)<0.5] <- 0
  counts <- 0
  for (i in 1:length(label)){
    if (label[i] == prob[i])
      counts <- counts + 1
  }
  acc <- counts/length(label)
  return(acc)
}
