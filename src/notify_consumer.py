import json

def handler(event, context):
    failures = []
    for record in event["Records"]:
        attempt = record.get("attributes", {}).get("ApproximateReceiveCount", "?")
        try:
            evt = json.loads(record["body"])
            todo = evt["data"]
            if "#fail" in todo["title"]:
                raise ValueError("fallo simulado: el título contiene #fail")
            print(f' [NOTIFICACION] Completado: "{todo["title"]}" ({todo["id"]})')
        except Exception as exc:
            print(f'[ERROR] mensaje {record["messageId"]} intento {attempt}: {exc}')
            failures.append({"itemIdentifier": record["messageId"]})
    return {"batchItemFailures": failures}
