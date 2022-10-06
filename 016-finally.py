def run():
  try:
    x = 1/0
  except FileNotFoundError as e:
    print(e)
  finally:
    print("execute this line")

run()