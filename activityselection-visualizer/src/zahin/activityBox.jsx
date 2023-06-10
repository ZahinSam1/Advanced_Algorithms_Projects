import { useEffect, useState } from "react";
import "./activityBox.css";

const ActivityBox = ({ ID }) => {
  const [boxID, setBoxID] = useState(0);
  useEffect(() => {
    setBoxID(ID);
  }, [ID]);
  return (
    <div className="activityBoxContainer">
      <p className="activityName">Activity {boxID}</p>
      <p className="activityStartTime">0</p>
      <p className="activityEndTime">10</p>
    </div>
  );
};

export default ActivityBox;
