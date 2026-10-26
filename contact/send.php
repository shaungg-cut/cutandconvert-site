<?php
// Cut & Convert audit request handler. Emails the submission, then redirects.

const TO_EMAIL   = 'shaunmalinao@gmail.com';
const FROM_EMAIL = 'no-reply@cutandconvert.com';
const THANKS_URL = '/contact/thanks/';
const ERROR_URL  = '/contact/?error=1';

function back(string $url): void {
    header('Location: ' . $url, true, 303);
    exit;
}

function clean(string $key, int $max = 500): string {
    $v = isset($_POST[$key]) && is_string($_POST[$key]) ? $_POST[$key] : '';
    $v = trim(str_replace(["\r", "\0"], '', $v));
    return mb_substr($v, 0, $max);
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    back('/contact/');
}

// Honeypot: bots fill hidden fields. Pretend success.
if (!empty($_POST['company_url'])) {
    back(THANKS_URL);
}

$name    = str_replace("\n", ' ', clean('name', 120));
$email   = str_replace("\n", '', clean('email', 200));
$phone   = str_replace("\n", ' ', clean('phone', 40));
$website = str_replace("\n", ' ', clean('website', 200));
$spend   = str_replace("\n", ' ', clean('spend', 60));
$message = clean('message', 4000);

$allowed  = ['Ecommerce', 'Local Business', 'YouTube Creative'];
$services = [];
if (isset($_POST['services']) && is_array($_POST['services'])) {
    foreach ($_POST['services'] as $s) {
        if (is_string($s) && in_array($s, $allowed, true)) {
            $services[] = $s;
        }
    }
}

if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    back(ERROR_URL);
}

$subject = 'New audit request: ' . $name . ($services ? ' (' . implode(', ', $services) . ')' : '');

$body  = "New audit request from cutandconvert.com\n\n";
$body .= "Name:      {$name}\n";
$body .= "Email:     {$email}\n";
$body .= "Phone:     " . ($phone !== '' ? $phone : '-') . "\n";
$body .= "Business:  " . ($website !== '' ? $website : '-') . "\n";
$body .= "Services:  " . ($services ? implode(', ', $services) : '-') . "\n";
$body .= "Ad spend:  " . ($spend !== '' ? $spend : '-') . "\n\n";
$body .= "Message:\n" . ($message !== '' ? $message : '-') . "\n";

$headers  = 'From: Cut & Convert <' . FROM_EMAIL . ">\r\n";
$headers .= 'Reply-To: ' . $email . "\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$encodedSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';

if (@mail(TO_EMAIL, $encodedSubject, $body, $headers, '-f' . FROM_EMAIL)) {
    back(THANKS_URL);
}
back(ERROR_URL);
