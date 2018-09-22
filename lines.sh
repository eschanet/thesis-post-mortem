for file in Introduction/introduction.tex Abstract/abstract.tex Acknowledgement/acknowledgement.tex Appendix1/appendix1.tex Appendix2/appendix2.tex Declaration/declaration.tex chapter-1lepton/1lepton.tex chapter-electroweak/electroweak.tex chapter-experiment/experiment.tex chapter-mc/mc.tex chapter-pmssm/pmssm.tex chapter-statistics/statistics.tex chapter-summary/summary.tex chapter-theory/theory.tex thesis.tex Preamble/preamble.tex; do

    log=$(git log --no-merges --pretty=tformat:'%ad' --date='format:day:%A hour:%H' --numstat $file | paste - - -)

    for day in Monday Tuesday Wednesday Thursday Friday Saturday Sunday; do
        log_day=$(echo "$log" | grep "day:$day" - | cut -f 3-4 | awk '{added += $1; deleted += $2} END {print added " " deleted}')
        name=$(echo $file | cut -d/ -f1)
        echo $name
        echo $day $log_day >> data-commit-days-$name
    done

    for hour in $(seq 0 23); do
        hour=$(printf %02d $hour)
        log_hour=$(echo "$log" | grep "hour:$hour" - | cut -f 3-4 | awk '{added += $1; deleted += $2} END {print added " " deleted}')
        name=$(echo $file | cut -d/ -f1)
        echo $hour $log_hour >> data-commit-hours-$name
    done

done
