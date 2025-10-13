---
front_matter_title: ""
layout: default
navigation_weight: 3
permalink: /project2/
title: Project 2
navigable_page_name: project2
---

# Project 2: Integrate the Help Desk UI with an API

This is a partially implemented React/TypeScript chat application frontend that you will complete by implementing API service methods

## Learning Outcomes

- Student can modify a React/TypeScript frontend application
- Student can read an API specification and implement service methods
- Student can use proper HTTP verbs to call API functions
- Student can implement authentication flows (login, registration, token management)
- Student is familiar with using fetch to call REST APIs
- Student can implement real-time chat features
- Student is introduced to working with React state management and component lifecycle

## Project Submission

{% if site.project2_submission %}

<{{site.project2_submission}}>

{% else %}

- Submission link will be posted at start of quarter

{% endif %}

## What's Included

- **Frontend**: React/TypeScript chat application with stubbed API services
- **Documentation**: API specification and assignment instructions (provided separately)

## Download the Project

Download the starter project: [project2.zip](/project2.zip)

## Quick Start

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start the development server**:
   ```bash
   npm run dev
   ```

3. **Open your browser** to `http://localhost:5173`

## Testing the Application

### Dummy Mode (Default)
The application comes with a dummy mode where all data is stored in the browsers localStorage.
You can test the UI using these dummy accounts by setting "Backend Mode" to "Dummy (Mock Data)" at `http://localhost:5173/settings`:

- **Username**: `alice` | **Password**: `password`
- **Username**: `bob` | **Password**: `password`
- **Username**: `charlie` | **Password**: `password`

The dummy backend should give you a feel for what the UI is supposed to do but it is not a completely functional backend.
If you ever want to reset the dummy data, clear all the keys from localStorage for this site in your browser.
From Chrome developer tools select Application > Local storage > http://localhost:5173 then clear:

- chat-app-config
- dummy-auth-config
- dummy-chat-data
- ...

### Switching to API Mode
To test your API implementations:

1. **Go to Settings** (Settings button in the header) or use the URL http://localhost:5173/settings if the button is not visible
2. **Change the Backend Mode** from "Dummy (Mock Data)" to "API (Real Backend)"
3. **Set the API Base URL** to: `https://project2backend.cs291.com`
4. **Double check that you used HTTPS not HTTP**
4. **Save the configuration**


### API Mode Testing
Once in API mode, you'll need to:
1. **Register new accounts** (the dummy accounts won't work with the real API)
2. **Test your API implementations** by using the application features
3. **Check browser dev tools** for any API errors

## Assignment Files

You should also have received these files with your assignment:
- `API_SPECIFICATION.md` - Complete API documentation

## What You Need to Implement

### API Service Integration
Implement all methods in:
- `src/services/implementations/ApiAuthService.ts`
- `src/services/implementations/ApiChatService.ts`

It is recommended to start with `ApiAuthService.ts` and get the registration, login, logout flow of the app working before continuing on to `ApiChatService.ts`

## Getting Help

1. Read the API specification thoroughly
2. Check existing service implementations for patterns
3. Use browser dev tools for debugging
4. Test API endpoints directly using tools like Postman
5. Look for similar questions on Piazza
6. Post to Piazza

## Required Tools

- [Node.js](https://nodejs.org/) and npm
- [React](https://react.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- Browser Developer Tools
- [Postman](https://www.postman.com/) or similar API testing tool

## Other Resources

- [React Documentation](https://react.dev/learn)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

Good luck with your implementation!
