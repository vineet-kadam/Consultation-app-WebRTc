import React from 'react'
import './SideBar.css'
import { IoIosChatboxes } from "react-icons/io";
import { MdSpeakerNotes } from "react-icons/md";
import { MdPerson } from "react-icons/md";
import { AiFillExclamationCircle } from "react-icons/ai";

const ApptDetails = ({ activeSidebar, setActiveSidebar, apptData }) => {
    const formatTime = (iso) => {
        if (!iso) return "--";
        return new Date(iso).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: true });
    };
    const formatDate = (iso) => {
        if (!iso) return "--";
        return new Date(iso).toLocaleDateString('en-GB');
    };

    return (
        <div className='sidebar-container'>
            {/* ── Tab Nav ── */}
            <div className='sidebar-nav'>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "chat" ? null : "chat")}>
                    <IoIosChatboxes />
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "notes" ? null : "notes")}>
                    <MdSpeakerNotes />
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "person" ? null : "person")}>
                    <MdPerson />
                </div>
                <div className='selected' onClick={() => setActiveSidebar(activeSidebar === "alert" ? null : "alert")}>
                    <AiFillExclamationCircle />
                    <span className='chat'>Appt. Details</span>
                </div>
            </div>

            {/* ── Content ── */}
            <div className='sidebar-content'>
                <div className='info-card'>
                    <div className='sname'>Department :</div>
                    <div className='pname'>{apptData?.department || "General"}</div>

                    <div className='sname'>Appointment type :</div>
                    <div className='pname'>{apptData?.appointment_type || "Video Consult"}</div>

                    <div className='sname'>Personnel :</div>
                    <div className='pname'>{apptData?.doctor_name ? `Dr. ${apptData.doctor_name}` : "N/A"}</div>

                    <div className='sname'>Appointment Reason :</div>
                    <div className='pname'>{apptData?.appointment_reason || "Other"}</div>

                    <div className='sname'>Date :</div>
                    <div className='pname'>{formatDate(apptData?.scheduled_time)}</div>

                    <div className='sname'>Time From :</div>
                    <div className='pname'>{formatTime(apptData?.scheduled_time)}</div>

                    <div className='sname'>Remark :</div>
                    <div className='pname'>{apptData?.remark || "No remarks provided."}</div>
                </div>
            </div>

            <div className='sidebar-bottom' />
        </div>
    )
}

export default ApptDetails