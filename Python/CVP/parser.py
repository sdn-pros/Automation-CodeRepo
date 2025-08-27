# parser.py
import argparse

class base:
    @staticmethod
    def parse_args():
        p = argparse.ArgumentParser(description="CloudVision gRPC Client")
        p.add_argument("--apiserver", required=True, help="e.g. 192.0.2.79:443")
        p.add_argument("--auth", required=True,
                       help="Format: token,token_file[,ca_file]  (3rd part is CA, not client cert)")

        args = p.parse_args()
        parts = args.auth.split(",")

        if len(parts) < 2:
            p.error("Invalid --auth. Use: token,token_file[,ca_file]")

        # Required
        args.tokenFile = parts[1]

        # Treat the optional 3rd value as CA bundle
        args.caFile = parts[2] if len(parts) > 2 else None

        # Ensure these exist so get_switches.py doesn't error
        args.certFile = None     # DO NOT pass a client cert
        args.keyFile  = None

        return args
