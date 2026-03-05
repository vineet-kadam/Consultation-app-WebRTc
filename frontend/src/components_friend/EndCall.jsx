import React from 'react'
import './EndCall.css'
import { IoIosCloseCircle } from "react-icons/io";
import { MdCallEnd } from "react-icons/md";
import { useNavigate } from 'react-router-dom';

const EndCall = ({ duration, summary, transcript }) => {
    const navigate = useNavigate();
    const role = localStorage.getItem("role");
    const isDoctor = role === "doctor";

    const goHome = () => {
        if (isDoctor) navigate("/doctor", { replace: true });
        else if (role === "patient") navigate("/patient", { replace: true });
        else navigate("/", { replace: true });
    };

    const viewTranscript = () => {
        // Open transcript in a new tab or show it — for now alert with content
        if (transcript) {
            const win = window.open("", "_blank");
            win.document.write(`<pre style="font-family:sans-serif;padding:24px;font-size:14px;line-height:1.7">${transcript}</pre>`);
        } else {
            alert("No transcript available for this session.");
        }
    };

    const fmt = s =>
        `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;

    return (
        <div className="wrapper">
            <div className='end-container'>
                {/* ── X closes to home ── */}
                <div className="end-navbar">
                    <div className="end-cross" onClick={goHome}>
                        <IoIosCloseCircle size={25} />
                    </div>
                </div>

                <div className="end-info">
                    <div className="end-call-info">
                        <div className="end-call-icon">
                            <MdCallEnd size={25} />
                        </div>
                        <div className='end-call-text'>Call Ended</div>
                        <div className="end-call-dur">
                            <div style={{ fontFamily: 'Montserrat', fontWeight: '500', fontSize: '13px', color: '#9E9E9E' }}>Call Duration : </div>
                            <div style={{ fontFamily: 'Montserrat', fontWeight: '600', fontSize: '15px', color: 'black' }}>{fmt(duration || 0)}</div>
                        </div>
                    </div>

                    <div className="end-summary">
                        <div style={{ fontFamily: 'Montserrat', fontWeight: '600', fontSize: '14px', color: 'black', marginBottom: '8px' }}>
                            AI Call Summary
                        </div>
                        <ul style={{ fontFamily: 'Montserrat', fontWeight: '500', fontSize: '12px', color: '#505050', margin: 0, paddingLeft: '16px' }}>
                            {summary && summary.length > 0 ? (
                                summary.map((item, idx) => <li key={idx}>{item}</li>)
                            ) : (
                                <>
                                    <li>Patient discussed symptoms and medical history.</li>
                                    <li>Personnel provided consultation and advised on next steps.</li>
                                    <li>Meeting concluded successfully.</li>
                                </>
                            )}
                        </ul>
                    </div>

                    {/* ── Buttons — doctor sees View Transcript, patient sees Back to Home ── */}
                    <div className="end-buttons">
                        {isDoctor ? (
                            <div className="button1" onClick={viewTranscript}>View Transcript</div>
                        ) : (
                            <div className="button1" onClick={goHome}>Back to Home</div>
                        )}
                        <div className="button2">✨ Scan Transcript for AI Insights</div>
                        <div className="button3" onClick={() => alert("Feedback request sent.")}>Ask for Feedback</div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default EndCall