"use client";

import Link from "next/link";
import React, { useState, ChangeEvent } from "react";

interface LoginForm {
  username: string;
  email: string;
  password: string;
}

export default function Signup() {
  const [form, setForm] = useState<LoginForm>({
    username: "",
    email: "",
    password: "",
  });

  function onChange(e: ChangeEvent<HTMLInputElement>) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  function onSignUpClick() {
    console.log("SignUp" + form.username + form.email + form.password);
  }

  return (
    <div>
      <h1>SignUp</h1>
      <div>
        <label>Your name</label>
        <input
          type="text"
          name="username"
          placeholder="Enter user name"
          value={form.username}
          onChange={onChange}
        />
      </div>

      <div>
        <label>Your email</label>
        <input
          type="text"
          name="email"
          placeholder="Enter email"
          value={form.email}
          onChange={onChange}
        />
      </div>

      <div>
        <label>Your password</label>
        <input
          type="password"
          name="password"
          placeholder="Enter password"
          value={form.password}
          onChange={onChange}
        />
      </div>

      <button onClick={onSignUpClick}>SignUp</button>

      <p>
        Already have an account? <Link href="/login">Login</Link>
      </p>
    </div>
  );
}
