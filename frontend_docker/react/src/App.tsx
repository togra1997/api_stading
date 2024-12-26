import { useState } from "react";
import "./App.css";

interface InputFieldProps {
  label: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder: string;
}

function InputField({ label, value, onChange, placeholder }: InputFieldProps) {
  return (
    <div className="card bg-gray-100 p-6 rounded-lg shadow-md">
      <input
        type="text"
        value={value}
        onChange={onChange}
        className="border border-gray-300 p-2 rounded w-full"
        placeholder={placeholder}
      />
      <p className="mt-4">
        {label}: {value}
      </p>
    </div>
  );
}

function App() {
  const [count, setCount] = useState(0);
  const [inputValue, setInputValue] = useState("");

  return (
    <div className="flex flex-col items-center gap-6 p-6">
      <h1 className="text-3xl font-bold underline">Vite + React</h1>
      <div className="card bg-gray-100 p-6 rounded-lg shadow-md">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700"
          onClick={() => setCount((count) => count + 1)}
        >
          count is {count}
        </button>
        <p className="mt-4">
          Edit <code className="bg-gray-200 p-1 rounded">src/App.tsx</code> and
          save to test HMR
        </p>
      </div>
      <InputField
        label="入力された文字"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Type something..."
      />
      <p className="text-gray-600">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  );
}

export default App;
