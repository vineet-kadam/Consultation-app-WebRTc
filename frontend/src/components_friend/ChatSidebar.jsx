import React, { useState, useRef, useEffect } from 'react'
import './SideBar.css'
import { IoIosChatboxes } from "react-icons/io";
import { MdSpeakerNotes } from "react-icons/md";
import { MdPerson } from "react-icons/md";
import { AiFillExclamationCircle } from "react-icons/ai";
import { BsSendFill } from "react-icons/bs";

const ChatSidebar = ({ activeSidebar, setActiveSidebar, messages, onSendMessage, myName }) => {
    const [inputValue, setInputValue] = useState("");
    const bottomRef = useRef(null);

    // Auto-scroll to latest message
    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    const handleSend = () => {
        if (inputValue.trim()) {
            onSendMessage(inputValue);
            setInputValue("");
        }
    };

    return (
        <div className='sidebar-container'>
            {/* ── Tab Nav ── */}
            <div className='sidebar-nav'>
                <div className='selected' onClick={() => setActiveSidebar(activeSidebar === "chat" ? null : "chat")}>
                    <IoIosChatboxes />
                    <span className='chat'>Chat</span>
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "notes" ? null : "notes")}>
                    <MdSpeakerNotes />
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "person" ? null : "person")}>
                    <MdPerson />
                </div>
                <div className='nselected' onClick={() => setActiveSidebar(activeSidebar === "alert" ? null : "alert")}>
                    <AiFillExclamationCircle />
                </div>
            </div>

            {/* ── Messages ── */}
            <div className='sidebar-content'>
                {messages.length === 0 && (
                    <p style={{ color: '#bbb', fontSize: 13, textAlign: 'center', marginTop: 24, fontStyle: 'italic' }}>
                        No messages yet. Say hello!
                    </p>
                )}
                {messages.map((msg, index) => {
                    const isSelf = msg.sender === myName;
                    return (
                        <div key={index} className={`chat-msg-row ${isSelf ? "self" : "other"}`}>
                            <div className='chat-sender-label'>
                                {isSelf ? `YOU  ${msg.timestamp}` : `${msg.sender}  ${msg.timestamp}`}
                            </div>
                            <div className={`chat-bubble ${isSelf ? "self" : "other"}`}>
                                {msg.text}
                            </div>
                        </div>
                    );
                })}
                <div ref={bottomRef} />
            </div>

            {/* ── Input ── */}
            <div className='sidebar-bottom'>
                <div className='input-box'>
                    <input
                        type='text'
                        placeholder='Type message here...'
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                    />
                    <div className='send' onClick={handleSend}>
                        <BsSendFill />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ChatSidebar