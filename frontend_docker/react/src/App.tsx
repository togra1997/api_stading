import { useState, useEffect } from "react";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Label } from "@/components/ui/label";
import axios from "axios";
import { Button } from "./components/ui/button";

import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

function App() {
  const [startTime, setStartTime] = useState("");
  const [endTime, setEndTime] = useState("");
  interface showBase {
    id: string;
    name: string;
  }

  const [tasks, setTasks] = useState<showBase[]>([]);
  const [task, setTask] = useState("");

  const [effortAssignments, setEffortAssignments] = useState<showBase[]>([]);
  const [effortAssignment, setEffortAssignment] = useState("");

  interface WorkTime {
    start: string;
    end: string;
    task: string;
    effort_assignment: string;
    date: string;
    id: number;
  }

  const [workTime, setWorkTime] = useState<WorkTime[]>([]);

  useEffect(() => {
    axios.get("http://localhost:8000/tasks").then((res) => {
      setTasks(res.data.data);
    });
    axios.get("http://localhost:8000/effort-assignment").then((res) => {
      setEffortAssignments(res.data.data);
    });
    axios.get("http://localhost:8000/work-time").then((res) => {
      setWorkTime(res.data.data);
    });
  }, []);

  function sendData(): void {
    axios
      .post("http://localhost:8000/work-time", {
        start: startTime,
        end: endTime,
        task: task,
        effort_assignment: effortAssignment,
      })
      .then((res) => {
        console.log({ startTime });
        console.log({ endTime });
        console.log({ task });
        console.log({ effortAssignment });
        setWorkTime(res.data);
        // window.location.reload(); // 画面を更新
      });
  }

  return (
    <>
      <div className="flex flex-col items-center justify-center bg-gray-100 p-4">
        <h1 className="mb-4 text-3xl font-bold text-gray-800">
          Time Input Form
        </h1>
      </div>
      <div className="flex flex-col items-center justify-center rounded-lg bg-white p-6 shadow-md">
        <div className="mb-4 flex space-x-4">
          <Label>開始時間</Label>
          <input
            className="rounded-md border border-gray-300 p-2"
            type="time"
            value={startTime}
            onChange={(e) => setStartTime(e.target.value)}
          />
          <Label>終了時間</Label>
          <input
            className="rounded-md border border-gray-300 p-2"
            type="time"
            value={endTime}
            onChange={(e) => setEndTime(e.target.value)}
          />
        </div>
        <div className="flex p-3">
          <Label>タスク</Label>
          <Select onValueChange={(value) => setTask(value)}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Theme" />
            </SelectTrigger>
            <SelectContent>
              {tasks.map((task) => (
                <SelectItem key={task.id} value={task.name}>
                  {task.name}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="flex p-3">
          <Label>工数付け先</Label>
          <Select onValueChange={(value) => setEffortAssignment(value)}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Theme" />
            </SelectTrigger>
            <SelectContent>
              {effortAssignments.map((task) => (
                <SelectItem key={task.id} value={task.name}>
                  {task.name}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
        <Button onClick={() => sendData()}>送信</Button>
      </div>
      <div className="container mt-4 flex bg-gray-100 p-4">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">ID</TableHead>
              <TableHead>経過工数</TableHead>
              <TableHead>タスク名</TableHead>
              <TableHead className="text-right">工数付け先</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {workTime.map((work) => (
              <TableRow key={work.id}>
                <TableCell className="font-medium">{work.id}</TableCell>
                <TableCell>
                  {work.start} - {work.end}
                </TableCell>
                <TableCell>{work.task}</TableCell>
                <TableCell className="text-right">
                  {work.effort_assignment}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </>
  );
}

export default App;
