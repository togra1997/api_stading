import { useState } from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";

function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState("");
  return (
    <>
      <div className="container none object-center text-center bg-gray-100">
        <h1 className="text-5xl p-5">Application</h1>
      </div>
      <div className="container md object-center text-center bg-blue-200">
        <div className="columns-2">
          <div className="container md object-center text-center bg-red-200">
            <TextField
              id="outlined-basic"
              label="Outlined"
              variant="outlined"
              onChange={(e) => setName(e.target.value)}
            />
            <p>your name:{name}</p>
          </div>
          <div className="container md object-center text-center bg-red-100">
            {/* <TextField
              id="outlined-basic"
              label="Outlined"
              variant="outlined"
            /> */}
            <input type="date" />
            <p>your name:{name}</p>
          </div>
        </div>

        <Button
          className="p-2"
          variant="contained"
          onClick={() => setCount(count + 1)}
        >
          Click me
        </Button>
        <p>count :{count}</p>
      </div>
    </>
  );
}

export default App;
