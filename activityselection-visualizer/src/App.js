import "./App.css";
// import BarChange from './components/test';
import HeapSortVisualizer from "./zahin/test";
import ActivityBox from "./zahin/activityBox";

function App() {
  return (
    <div className="container">
      {/* <HeapSortVisualizer /> */}
      <ActivityBox ID={1}/>
      <ActivityBox ID={2} />
      <ActivityBox ID={3} />
      <ActivityBox ID={4} />
      <ActivityBox ID={5} />
      <ActivityBox ID={6} />
      <ActivityBox ID={7} />
      <ActivityBox ID={8} />
      <ActivityBox ID={9} />
      <ActivityBox ID={10} />
      <ActivityBox ID={11} />
      <ActivityBox ID={12} />
    </div>
  );
}

export default App;
