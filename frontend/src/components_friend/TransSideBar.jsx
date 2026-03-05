import React from 'react'
import './SideBar.css'
import { IoIosChatboxes } from "react-icons/io";
import { MdSpeakerNotes } from "react-icons/md";
import { MdPerson } from "react-icons/md";
import { AiFillExclamationCircle } from "react-icons/ai";

const TransSideBar = ({ activeSidebar, setActiveSidebar, notes }) => {
    return (
        <div className='sidebar-container'>
            {/* ── Tab Nav ── */}
            <div className='sidebar-nav'>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "chat" ? null : "chat")}>
                    <IoIosChatboxes />
                </div>
                <div className='selected' onClick={() => setActiveSidebar(activeSidebar === "notes" ? null : "notes")}>
                    <MdSpeakerNotes />
                    <span className='chat'>Transcript</span>
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "person" ? null : "person")}>
                    <MdPerson />
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "alert" ? null : "alert")}>
                    <AiFillExclamationCircle />
                </div>
            </div>

            {/* ── Transcript lines ── */}
            <div className='sidebar-content'>
                {notes && notes.length > 0 ? (
                    notes.map((note, index) => (
                        <div key={index} className='transcript-line'>
                            <span style={{ fontWeight: 600, color: '#9E9E9E' }}>{note.speaker}: </span>
                            <span style={{ color: '#353535' }}>{note.text}</span>
                        </div>
                    ))
                ) : (
                    <p style={{ color: '#bbb', fontStyle: 'italic', fontSize: 13, textAlign: 'center', marginTop: 24 }}>
                        Live transcript will appear here...
                    </p>
                )}
            </div>

            <div className='sidebar-bottom' />
        </div>
    )
}

export default TransSideBar