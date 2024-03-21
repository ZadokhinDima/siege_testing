## App description
When receiving /save request application saves document with random string name to mongo DB collection. Also after save it fetches all documents with name that starts with same two characters.

## Siege
Siege is running in docker container because it was problematic to set it up on Windows. siege.out contains output for different siege runs.

## Result table

| Concurrency | Availability | Avg Response Time | Throughput |
|-------------|--------------|------------------|------------|
|       10    | 100.00 %     | 0.02 secs        |0.01 MB/sec |
|       25    | 100.00 %     | 0.02 secs        |0.01 MB/sec |
|       50    | 100.00 %     | 0.02 secs        |0.03 MB/sec |
|       100   | 100.00 %     | 0.03 secs        |0.05 MB/sec |
