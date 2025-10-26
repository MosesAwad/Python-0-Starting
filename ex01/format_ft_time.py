import time

# Date of the epoch
epoch_date = time.gmtime(0)
epoch_date_str = time.strftime("%B %-d, %Y", epoch_date)

# Seconds since the epoch
seconds_since_epoch = time.time()

# Local date
localdate = time.localtime(seconds_since_epoch)
localdate_str = time.strftime("%b %d %Y",localdate)

print(f"Seconds since {epoch_date_str}:", f"{seconds_since_epoch:,.4f}", "or", f"{seconds_since_epoch:.2e}", "in scientific notation")
print(localdate_str)