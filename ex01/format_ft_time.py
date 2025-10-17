import time

epoch = time.gmtime(0)
epoch_str = time.strftime("%B %-d, %Y", epoch)

seconds_since_epoch = time.time()

localdate = time.localtime(time.time())
localdate_str = time.strftime("%b %d %Y",localdate)

print(f"Seconds since {epoch_str}:", f"{seconds_since_epoch:,.4f}", "or", f"{seconds_since_epoch:.2e}", "in scientific notation")
print(localdate_str)