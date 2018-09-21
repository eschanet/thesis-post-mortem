log=$(git log --no-merges --pretty=tformat:'%ad' --date='format:day:%A hour:%H' --numstat **/*tex | paste - - -)

for day in Monday Tuesday Wednesday Thursday Friday Saturday Sunday; do
    log_day=$(echo "$log" | grep "day:$day" - | cut -f 3-4 | awk '{added += $1; deleted += $2} END {print added " " deleted}')
    echo $day $log_day >> data-commit-days
done

for hour in $(seq 0 23); do
    hour=$(printf %02d $hour)
    log_hour=$(echo "$log" | grep "hour:$hour" - | cut -f 3-4 | awk '{added += $1; deleted += $2} END {print added " " deleted}')
    echo $hour $log_hour >> data-commit-hours
done
