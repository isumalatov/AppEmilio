"use client";

import Link from "next/link";
import React, { useState, ChangeEvent } from "react";

interface LoginForm {
  username: string;
  password: string;
}

export default function Login() {
  const [form, setForm] = useState<LoginForm>({
    username: "",
    password: "",
  });

  function onChange(e: ChangeEvent<HTMLInputElement>) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  function onLoginClick() {
    console.log("Login" + form.username + form.password);
  }

  return (
    <div>
      <h1>Login</h1>
      <div>
        <label>User name</label>
        <input
          type="text"
          name="username"
          placeholder="Enter user name"
          value={form.username}
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

      <button onClick={onLoginClick}>Login</button>

      <p>
        Don't have an account? <Link href="/signup">SignUp</Link>
      </p>
    </div>
  );
}
