gcloud sql import csv test1 gs://exo-import-data-bdd-csv/users_data.csv \
  --database=postgres \
  --table=users \
  --csv-import-options="skipLeadingRows=1" \
  --quiet