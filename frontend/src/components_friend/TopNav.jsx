import React from "react";
import './minScreen.css'
import { TbArrowsDiagonalMinimize2 } from "react-icons/tb";
import { FiMaximize2 } from "react-icons/fi";

const TopNav = ({ isMini, setIsMini }) => {
  return (
    <div className={`${isMini ? "min-navbar" : "max-navbar"}`}>
      {/* Title — left */}
      <div style={{ fontFamily: 'Montserrat', fontWeight: '680', fontSize: '18px', color: '#232323' }}>
        Video Call
      </div>

      {/* Minimize / Maximize button — RIGHT corner (flex space-between in max-navbar CSS) */}
      <div
        style={{
          border: '1px solid #ccc',
          width: '26px', height: '24px',
          display: 'flex', justifyContent: 'center', alignItems: 'center',
          borderRadius: '6px', cursor: 'pointer',
          background: '#f8fafc', color: '#555',
          flexShrink: 0,
        }}
        onClick={() => setIsMini(!isMini)}
        title={isMini ? "Expand" : "Minimize"}
      >
        {isMini ? <FiMaximize2 size={13} /> : <TbArrowsDiagonalMinimize2 size={13} />}
      </div>
    </div>
  );
};

export default TopNav;