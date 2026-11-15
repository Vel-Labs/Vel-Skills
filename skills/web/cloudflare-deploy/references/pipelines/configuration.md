<!-- Vel-Skills removed implicit CLI downloads and remote shell execution. -->
# Pipelines Configuration

## Worker Binding

```jsonc
// wrangler.jsonc
{
  "pipelines": [
    { "pipeline": "<STREAM_ID>", "binding": "STREAM" }
  ]
}
```

Get stream ID: `wrangler pipelines streams list`

## Schema (Structured Streams)

```json
{
  "fields": [
    { "name": "user_id", "type": "string", "required": true },
    { "name": "event_type", "type": "string", "required": true },
    { "name": "amount", "type": "float64", "required": false },
    { "name": "timestamp", "type": "timestamp", "required": true }
  ]
}
```

**Types:** `string`, `int32`, `int64`, `float32`, `float64`, `bool`, `timestamp`, `json`, `binary`, `list`, `struct`

## Stream Setup

```bash
# With schema
wrangler pipelines streams create my-stream --schema-file schema.json

# Unstructured (no validation)
wrangler pipelines streams create my-stream

# List/get/delete
wrangler pipelines streams list
wrangler pipelines streams get <ID>
wrangler pipelines streams delete <ID>
```

## Sink Configuration

**R2 Data Catalog (Iceberg):**
```bash
wrangler pipelines sinks create my-sink \
  --type r2-data-catalog \
  --bucket my-bucket --namespace default --table events \
  --catalog-token $TOKEN \
  --compression zstd --roll-interval 60
```

**R2 Raw (Parquet):**
```bash
wrangler pipelines sinks create my-sink \
  --type r2 --bucket my-bucket --format parquet \
  --path analytics/events \
  --partitioning "year=%Y/month=%m/day=%d" \
  --access-key-id $KEY --secret-access-key $SECRET
```

| Option | Values | Guidance |
|--------|--------|----------|
| `--compression` | `zstd`, `snappy`, `gzip` | `zstd` best ratio, `snappy` fastest |
| `--roll-interval` | Seconds | Low latency: 10-60, Query perf: 300 |
| `--roll-size` | MB | Larger = better compression |

## Pipeline Creation

```bash
wrangler pipelines create my-pipeline \
  --sql "INSERT INTO my_sink SELECT * FROM my_stream WHERE event_type = 'purchase'"
```

**⚠️ Pipelines are immutable** - cannot modify SQL. Must delete/recreate.

## Credentials

| Type | Permission | Get From |
|------|------------|----------|
| Catalog token | R2 Admin Read & Write | Dashboard → R2 → API tokens |
| R2 credentials | Object Read & Write | `wrangler r2 bucket create` output |
| HTTP ingest token | Workers Pipeline Send | Dashboard → Workers → API tokens |

## Complete Example

```bash
wrangler r2 bucket create my-bucket
wrangler r2 bucket catalog enable my-bucket
wrangler pipelines streams create my-stream --schema-file schema.json
wrangler pipelines sinks create my-sink --type r2-data-catalog --bucket my-bucket ...
wrangler pipelines create my-pipeline --sql "INSERT INTO my_sink SELECT * FROM my_stream"
wrangler deploy
```
