#!/usr/bin/env python3
import argparse, json, random, time, sys, string
from datetime import datetime, timezone
try:
    from kafka import KafkaProducer
except Exception as e:
    print("ERROR: kafka-python is required. Install with: pip install kafka-python", file=sys.stderr)
    raise

def rand_id(prefix="u", k=8):
    return prefix + ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))

def main():
    ap = argparse.ArgumentParser(description="Kafka demo producer")
    ap.add_argument("--brokers", default="localhost:9092", help="Bootstrap servers")
    ap.add_argument("--topic", default="events", help="Kafka topic")
    ap.add_argument("--rate", type=float, default=5, help="events per second")
    args = ap.parse_args()

    producer = KafkaProducer(bootstrap_servers=args.brokers,
                             value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    print(f"Producing to {args.topic} at ~{args.rate} eps. Ctrl+C to stop.")
    try:
        while True:
            event = {
                "event_time": datetime.now(timezone.utc).isoformat(),
                "user_id": rand_id("u"),
                "action": random.choice(["view","click","purchase","add_to_cart"]),
                "item_id": rand_id("i"),
                "price": round(random.uniform(5, 200), 2),
                "source": random.choice(["web","ios","android"])
            }
            producer.send(args.topic, event)
            producer.flush()
            time.sleep(1.0 / max(args.rate, 0.1))
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        producer.close()

if __name__ == "__main__":
    main()
