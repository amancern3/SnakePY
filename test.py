from guy import Guy

class App(Guy):
  """
  <head>
    <style>
        body {
            padding: 8px,
            text-align: center; /* center the text */
            background: #1abc9c; /* green background */
            color: white; 
        }
    <style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }
    </style>
  </head>
  <h1>Game Launcher</h1>
  
  <button onclick="call()">Snake Game</button>
  
  <hr/>
  
  <script>
  async function call() {
    var txt=await self.test()
    document.body.innerHTML += txt + "<br/>";
  }

  </script>
  """

  def test(self):
      import datetime
      sendthis =  datetime.datetime.now()
      self.test_snake(self)
      return sendthis

  def test_snake(self):
      import snake
      snake.main()
      return

if __name__ == "__main__":
    App().serve()
